@extends('admin.layout')

@section('styles')
<style>
  .custom_portfolio_name{
    width: 80%;
    padding: 19px 0px;
  }
</style>
@endsection

@section('content')
    <div id="content" class="">

        <h1>Select Articles to change</h1>
        <div id="content-main">
            <ul class="object-tools">
                <li>
                    <a href="{{ route('admin.add_article') }}" class="addlink">
                        Add Articles
                    </a>
                </li>
            </ul>
            <div class="module" id="changelist">
                <div class="changelist-form-container">
                    <div class="results">
                        <table id="result_list">
                            <thead>
                                <tr>
                                    <th scope="col" class="column-__str__">
                                     <div class="text"><span>Portfolios</span></div>
                                    </th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                @foreach($articles as $article)
                                    <tr>
                                        <td class="field-__str__ custom_portfolio_name">
                                            <a style="color: black" href="{{ route('admin.update_article', [$article]) }}">{{ $article->name }}</a>
                                        </td>
                                        <td>
                                            <span><a href="{{ route('admin.delete_article', [$article]) }}" class="btn btn-danger">Delete</a></span>
                                        </td>
                                    </tr>
                                @endforeach
                            </tbody>
                        </table>
                    </div>
                    <p class="paginator">

                    </p>
                </div>
            </div>
        </div>
        <br class="clear">
    </div>
@endsection
