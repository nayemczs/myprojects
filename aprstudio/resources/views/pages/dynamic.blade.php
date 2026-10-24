@extends('layout')
@section('styles')
<style>
    .background_body {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .middle_one {
        position: absolute;
        top: 90vh;
        z-index: 7;
    }

    .custom_writing_text {
        left: -46px;
    }

    .hero_image {
        position: fixed;
        bottom: 0;
        width: 100%;
        height: 0;
        opacity: 0;
        transition: height ease-in-out 0.25s, opacity ease-in-out 0.25s;
    }

    .hero_image.show {
        height: 100%;
        opacity: 1;
    }

    .hero_image .image_overlay {
        position: absolute;
        top: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(180deg, rgba(92, 92, 92, 0) 0%, rgba(255, 255, 255, 1) 70%);
    }
    .middle_two {
        position: fixed;
        bottom: 7%;
        z-index: 7;

    }
    .hero_image img {
        width: 100%;
        height: 75%;
        object-fit: cover;
    }
    a:hover{
        color: black;
    }


</style>
@endsection
@section('body')
<section class="container" id="description">
    <div class="row">
        <div class="col-md-10 mx-auto">
            <div class="row" style="padding: 0">
                <div class="col-md-3 custom_dynamic_para1 ps-4">
                    <h2>{{ $article->name }}</h2>
                    <p>{{ $article->short_description }}</p>
                </div>
                <div class="col-md-9">
                    <div class="custom_dynamic_para2">
                        <p>{{ $article->description }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<div class="middle_two" id="scroll_down">
    <a href="#project"><img src="/img/Group.svg" width="23" alt=""></a>
</div>
<div class="left_sidebar left_middle">
    <p class="scrolltotop"><i class="fas fa-arrow-up"></i></p>
    <p> <a href="{{ route('index') }}"><i class="fas fa-arrow-left"></i></a></p>
    <p class="custom_writing_text">{{ $article->get_category_display() }}</p>
</div>
<div class="right_sidebar right_middle">
    <p class="text-start right_option"><a href="#description">Description</a> <span>
        <i class="fas fa-circle custom_circle_icon ps-2" id="circle_black"></i></span></p>
    <p class="text-start right_option"><a href="#project">Project</a><span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
</div>
<div class="right_sidebar next_arrow">
    <p>Next<span class="ps-2"><i class="fas fa-arrow-right"></i></span></p>
</div>
<section class="container">
    <div class="row my-4" style="padding: 0">
        <div class="col-md-10 mx-auto text-center">
            <img id="cover_image" src="{{ $article->image_url() }}" class="img-fluid" style="max-width: 715px" alt="">
        </div>
    </div>
</section>
<section class="hero_image" id="hero_image">
    <img src="{{ $article->image_url() }}" alt="">
    <div class="image_overlay"></div>
</section>
<section class="container">
    @foreach($article->images as $image)
    <div class="row" id="project" style="padding: 0; padding-bottom: 23px; margin: 0">
        <div class="col-md-10 mx-auto text-center">
            <img src="{{ $image->url() }}" class="img-fluid w-100" style="max-width: 715px" alt="">
        </div>
    </div>
    @endforeach
</section>
@endsection

@section('scripts')
<script>
    const descriptionContainer = document.querySelector('#cover_image')
    const heroImage = document.querySelector('#hero_image')
    const scrollDown = document.querySelector('#scroll_down')

    document.addEventListener('scroll', () => {
        if (descriptionContainer.getBoundingClientRect().bottom < 0) {
            heroImage.classList.add('show')
            scrollDown.style.display = 'none'
        }
        else {
            heroImage.classList.remove('show')
            scrollDown.style.display = 'block'
        }
    })

</script>
@endsection
