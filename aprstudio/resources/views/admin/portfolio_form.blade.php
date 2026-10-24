@extends('admin.layout')

@section('styles')
<style>
    table{
        width: 100%;
    }

    td {
        vertical-align: middle;
    }

    .is-invalid {
        border: 1px solid red !important;
    }


</style>
@endsection

@section('content')
    <!-- Content -->
    <div id="content" class="colM">
        @if($article)
            <h1>Update Article</h1>
        @else
            <h1>Add Article</h1>
        @endif
        <div id="content-main">
            <form method="POST" id="watch_form" enctype="multipart/form-data">
                @csrf

                <div>
                    <fieldset class="module aligned ">
                        <div class="form-row">
                            <div>
                                <label class="required" for="id_name">Name:</label>
                                <input type="text"
                                       name="name"
                                       value="{{ old('name', $article->name ?? '') }}"
                                       class="vTextField @error('name') is-invalid @enderror"
                                       maxlength="255"
                                       required
                                       id="id_name">
                                @error('name')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                        </div>
                        <div class="form-row">
                            <div>
                                <label class="required" for="id_category">Category:</label>
                                <div class="related-widget-wrapper">
                                    <select name="category" required id="id_category" class="@error('category') is-invalid @enderror">
                                        @foreach($category_choices as $category_choice)
                                            <option value="{{ $category_choice[0] }}"
                                            @if($category_choice[0] == old('category', $article->category ?? '')) selected @endif>
                                                {{ $category_choice[1] }}
                                            </option>
                                        @endforeach
                                    </select>
                                </div>
                                @error('category')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                        </div>
                        <div class="form-row">
                            <div>
                                <label class="required" for="id_short_description">Short Description:</label>
                                <input type="text"
                                       name="short_description"
                                       value="{{ old('short_description', $article->short_description ?? '') }}"
                                       class="vTextField @error('short_description') is-invalid @enderror"
                                       maxlength="255"
                                       required
                                       id="id_short_description">
                                @error('short_description')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                        </div>
                        <div class="form-row">
                            <div>
                                <label class="required" for="id_description">Description:</label>
                                <input type="text"
                                       name="description"
                                       value="{{ old('description', $article->description ?? '') }}"
                                       class="vTextField @error('description') is-invalid @enderror"
                                       required
                                       id="id_description">
                                @error('description')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                        </div>
                    </fieldset>

                    <fieldset class="module">
                        <h2>Cover Picture</h2>

                        <table>
                            <thead>
                            <tr>
                                <th class="original">Picture</th>
                                <th class="column-item required">Update</th>
                            </tr>
                            </thead>

                            <tbody>
                            <tr class="form-row">
                                <td class="original">
                                    @if($article)
                                        <img src="{{ $article->image_url() }}" width="80" alt="">
                                    @endif
                                </td>

                                <td class="field-item">
                                    <input type="file"
                                           accept="image/*"
                                           name="cover_picture"
                                           class="@error('cover_picture') is-invalid @enderror"
                                           id="id_cover_picture">
                                    @error('cover_picture')
                                        <ul class="errorlist"><li>{{ $message }}</li></ul>
                                    @enderror
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </fieldset>

                    <fieldset class="module">
                        <h2>Images</h2>

                        <table>
                            <thead>
                                <tr>
                                    <th class="original">Image</th>
                                    <th class="column-item required"></th>
                                    <th class="text-center">Delete?</th>
                                </tr>
                            </thead>

                            <tbody id="images_section">
                                @if($article)
                                    @foreach($article->images as $image)
                                        <tr class="form-row">
                                            <td class="original">
                                                <img src="{{ $image->url() }}" width="80" alt="">
                                            </td>

                                            <td class="field-item"></td>

                                            <td class="delete text-center">
                                                <input type="checkbox" name="delete_images[]" value="{{ $image->id }}">
                                            </td>
                                        </tr>
                                    @endforeach
                                @endif

                                @error('images')
                                   <tr><ul class="errorlist"><li>{{ $message }}</li></ul></tr>
                                @enderror

                                <tr class="add-row" id="insert_image">
                                    <td colspan="12"><a style="cursor: pointer" id="add_another_img">Add another Image</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </fieldset>
                    <div class="submit-row">
                        @if($article)
                            <p class="deletelink-box"><a href="{{ route('admin.delete_article', [$article]) }}" class="btn btn-danger">Delete</a></p>
                        @endif
                        <input type="submit" value="Save" class="default" name="_save">
                        <input type="submit" value="Save and add another" name="_add_another">
                        <input type="submit" value="Save and continue editing" name="_continue">
                    </div>
                </div>
            </form>
        </div>


        <br class="clear">
    </div>
@endsection

@section('scripts')
    <script>
        const addAnotherImage = document.querySelector('#add_another_img')
        const imageSection = document.querySelector('#images_section')
        const insertMarker = document.querySelector('#insert_image')

        addAnotherImage.addEventListener('click', () =>{
            const tr = document.createElement('tr')
            tr.innerHTML= `
                <td></td>
                <td class="field-item">
                    <p class="file-upload">
                        <input type="file" name="images[]" accept="image/*">
                    </p>
                </td>
                <td></td>
            `

            tr.classList.add('form-row')
            imageSection.insertBefore(tr, insertMarker)
        })
    </script>
@endsection
