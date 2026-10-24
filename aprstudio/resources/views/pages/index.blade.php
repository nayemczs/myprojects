@extends('layout')
@section('styles')
<style>

</style>
@endsection
@section('body')
<section id="portfolio-section" class="page bg-style1" style="">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="portfolio">
                    <!-- Begin page header-->
                    <div class="page-header-wrapper">
                        <div class="container p-0">
                            <div class="page-header wow fadeInDown" data-wow-delay="0.4s">
                                <h2>HI, I’m Ali</h2>
                                <p class="subtitle font-bold">A Product Designer based in NYC </p>
                                <p>I’m passionate about using <strong>qualitative and quantitative</strong> data to deliver novel
                                    insights for product research and leverage my role as a <strong>design thinker</strong> 
                                     </p>
                            </div>
                        </div>
                    </div>
                    <!-- End page header-->
                    <div class="portfoloi_content_area">
                        <div class="portfolio_menu" id="filters">
                            <ul class="custom_menu_ul">
                                <li class="active_prot_menu"><a href="#porfolio_menu" data-filter=".product_design">Product Design</a></li>
                                <li><a href="#porfolio_menu" data-filter=".brand_design">Brand design</a></li>
                                <li><a href="#porfolio_menu" data-filter=".photography">Photography</a></li>
                                <li><a href="#porfolio_menu" data-filter=".GraphicDesign">graphic design</a></li>
                                <li><a href="#porfolio_menu" data-filter=".about_me">About me</a></li>

                            </ul>
                        </div>
                        <div class="portfolio_content">
                            <div class="row" id="portfolio">
                                @foreach($brand_articles as $article)
                                <div class="col-xs-12 col-sm-4 brand_design">
                                    <div class="portfolio_single_content">
                                        <img src="{{$article->image_url()}}" alt="{{$article->name}}" />
                                        <div>
                                            <a href="{{route('show_article',[$article])}}">{{$article->name}}</a>
                                            <span>{{$article->short_description}}</span>
                                        </div>
                                    </div>
                                </div>
                                @endforeach
                                @foreach($graphic_articles as $article)
                                <div class="col-xs-12 col-sm-4 GraphicDesign">
                                    <div class="portfolio_single_content">
                                        <img src="{{$article->image_url()}}" alt="{{$article->name}}" />
                                        <div>
                                            <a href="{{route('show_article',[$article])}}">{{$article->name}}</a>
                                            <span>{{$article->short_description}}</span>
                                        </div>
                                    </div>
                                </div>
                                @endforeach
                                @foreach($photography_articles as $article)
                                <div class="col-xs-12 col-sm-4 photography">
                                    <div class="portfolio_single_content">
                                        <img src="{{$article->image_url()}}" style="height: 371px; width: 371px;
                                        object-fit: cover;" alt="{{$article->name}}" />
                                        <div class="d-flex">
                                            <p>{{$article->name}}</p>
                                            <a href="{{route('show_article',[$article])}}">Visit Case Study</a>
                                    </div>
                                    </div>
                                </div>
                                @endforeach

                                <div class="col-xs-12 col-sm-4 about_me">
                                    <div class="portfolio_single_content">
                                        <img src="/img/portfolio/rec9.png" alt="title" />
                                        <div>
                                            <a href="#">Last Motel</a>
                                            <span>Subtitle</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xs-12 col-sm-4 product_design">
                                    <div class="portfolio_single_content">
                                        <img src="/img/thumnail/logmeonce.png" alt="" />
                                        <div class="d-flex">
                                            <p>LOGMEONCE</p>
                                            <a href="{{ route('logmeonce') }}">Visit Case Study</a>
                                    </div>
                                    </div>
                                </div>
                                <div class="col-xs-12 col-sm-4 product_design">
                                    <div class="portfolio_single_content">
                                        <img src="/img/thumnail/natural.png" alt="" />
                                        <div class="d-flex">
                                            <p>NATURAL MUSEUM OF HISTORY</p>
                                            <a href="{{ route('natural') }}">Visit Case Study</a>
                                    </div>
                                    </div>
                                </div>
                                <div class="col-xs-12 col-sm-4 product_design">
                                    <div class="portfolio_single_content">
                                        <img src="/img/thumnail/begood.png" alt="" />
                                        <div class="d-flex">
                                            <p>BEGOOD</p>
                                            <a href="{{ route('begood') }}">Visit Case Study</a>
                                    </div>
                                    </div>
                                </div>
                                <div class="col-xs-12 col-sm-4 product_design">
                                    <div class="portfolio_single_content">
                                        <img src="/img/thumnail/aimate.png" alt="" />
                                        <div class="d-flex">
                                            <p>AIMATE</p>
                                            <a href="{{ route('aimate') }}">Visit Case Study</a>
                                    </div>
                                    </div>
                                </div>

                                <div class="col-xs-12 col-sm-4 about_me">
                                    <div class="portfolio_single_content">
                                        <img src="/img/portfolio/Rec8.png" alt="title" />
                                        <div>
                                            <a href="#">Old is Gold</a>
                                            <span>Subtitle</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</section>
<!-- End portfolio -->
<section class="container">
    <div class="row">
        <div class="col-lg-6 col-12 text-center">
            <img src="/img/banner-1.png" class="img-fluid" alt="">
        </div>
        <div class="col-lg-6 col-12 text-center">
            <img src="/img/banner-2.png" class="img-fluid" alt="">
        </div>
    </div>
</section>
<section class="container mt-5 bg-white py-5 px-5">
    <h2 class="">ToolBox</h2>
    <p class="">There are some of the tools I love to use</p>
    <div class="row">
        <div class="col-md-12">
            <div class="custom_logos py-4">
                <div class="custom_logo">
                    <img src="/img/logo/1.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/2.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/3.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/4.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/5.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/6.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/7.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/8.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/9.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/10.png" class="" alt="">
                </div>
            </div>
            <div class="custom_logos pt-5">
                <div class="custom_logo">
                    <img src="/img/logo/11.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/12.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/13.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/14.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/15.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/16.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/17.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/18.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/19.png" class="" alt="">
                </div>
                <div class="custom_logo">
                    <img src="/img/logo/last.png" class="" alt="">
                </div>
            </div>
        </div>

    </div>
</section>
<section class="container py-5">
    <div class="row">
        <div class="col-md-12 text-center cus_footer">
            <p>Let's Get In Touch</p>
        </div>

    </div>
</section>




@endsection

@section('scripts')
<script>
    window.onload = () => {
        document.querySelector('.active_prot_menu a').click()
    }

</script>
@endsection
