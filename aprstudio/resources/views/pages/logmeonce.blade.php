@extends('layout')
@section('styles')
<style>
    .text_end {
        position: absolute;
        top: 35px;
        right: 41px;
        z-index: 100;
    }

    .bottom {
        top: 60vh
    }

    .main_header_static {
        margin-bottom: 23px
    }

    .background_body {
        background-color: #F5AA39;
        background-image: none;
    }

    .static_para {
        color: #000;
        font-size: 19px;
        line-height: 26px;
    }

    .overlay {
        position: absolute;
        top: 0;
        width: 100%;
        height: 356px;
        background: linear-gradient(180deg, rgba(196, 196, 196, 0) 0%, rgba(245, 170, 57, 0.8) 70.83%);
    }

    .problem_solution {
        background: #EEEEEE;
        padding: 100px 180px 100px 180px;
    }

    .do_dont {
        padding: 65px 180px 20px 180px;
    }

    .related_web {
        padding: 0px 180px 100px 180px;
    }

    .problem_solution p {
        font-size: 24px;
        line-height: 33px;
        color: #000000;
    }

    .problem_solution h2 {
        font-weight: bold;
        font-size: 36px;
        line-height: 49px;
        color: #014AFF;
        margin-bottom: 40px
    }

    .custom_solution p {
        padding-left: 70px
    }

    .custom_solution h2 {
        padding-left: 70px
    }

    .custom_problem p {
        padding-right: 80px
    }

    .offer_you p {
        padding-right: 30px
    }

    .dont_offer p {
        padding-left: 30px
    }

    .custom_offer {
        font-size: 22px !important;
        line-height: 30px !important;
        color: #014AFF !important;
        margin-bottom: 5px;
    }

    .custom_research h2 {
        font-weight: bold;
        font-size: 40px !important;
        line-height: 48px;
        text-align: left;
    }

    .custom_research p {
        font-size: 34px !important;
        line-height: 41px !important;
    }

    .interview p {
        font-size: 22px;
        line-height: 30px;
        color: #000000;
    }

    .custom_personas p {
        font-size: 16px;
        line-height: 20px
    }

    .logo_edit {
        margin-top: 28px;
        margin-bottom: 35px;
    }

    .color_edit {
        margin-bottom: 110px;
    }

    .custom_footer {
        background-image: url(../img/static/footer_banner.png);
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
    }

    .custom_flow {
        background: #3842F2;
        color: white;
    }

    .flow_btns {
        margin-top: 45px;
        text-align: center;
        display: flex;
        flex-direction: column;
        /* justify-content: center; */
        align-items: center;
    }

    .custom_flow {}

    .custom_flow h2 {
        color: white;
        font-size: 28px;
        line-height: 27px;
        margin-top: 100px;
    }

    .common_btn {
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-sizing: border-box;
        border-radius: 10px !important;
        display: block;
        padding: 10px 20px;
        margin-bottom: 24px;
        color: #3842F2;
    }

    .btn_eclipse {
        border-radius: 25px !important;
    }

    .btn_third {
        background: rgba(255, 255, 255, 0.9);
    }

    .btn_four {
        background: rgba(255, 255, 255, 0.5);
        color: white;
    }

    .btn_five {
        background: rgba(255, 255, 255, 0.2);
        color: white;
    }

    .btn_six {
        background: rgba(255, 255, 255, 0.05);
        color: white;
    }

    .right_option {}


</style>
@endsection
@section('body')
<section class="container pb-4" style="">
    <div class="row">
        <div class="col-md-10 mx-auto">
            <h2 class="main_header_static">LOGMEONCE</h2>
            <div class="row" style="padding: 0">
                <div class="col-md-6 custom_dynamic_para1 static_para">
                    <p class="static_text text-white">Description</p>
                    <p>We want to be well informed but it is taking a toll on our well-being. 
                        Disaster news is the number one category in the news interest index and 
                        there are studies proving that exposure to bad news can cause anxiety, 
                        mood disorders and can even be addictive. There are reasons why news is 
                        bad for us: It disrupts our thinking, it changes our brain, it’s stressful. 

                    </p>
                    <p class="static_text text-white mt-5 mb-1">Deliverables</p>
                    <p class="">Branding, App & Web Design, Social Media Design</p>
                </div>
                <div class="col-md-6">
                    <div class="custom_dynamic_para2  static_para">
                        <p class="static_text text-white">My Role</p>
                        <p>Visual & Interaction Design
                            Information Architecture
                            Low-Fi & High-Fi Prototype Testing
                            Motion & Animation Design
                            Design System
                            Design Operation and Strategy
                            Qualitative & Quantitative Research
                        </p>
                        <p class="static_text text-white mt-5 mb-1">Tools</p>
                        <p class="">Figma, Framer, Adobe Creative Suite, Google Suite, </p>
                        <p class="static_text text-white mt-2 mb-1">Duration</p>
                        <p class="">Nov 2020 - Oct 2021 (8 Months)</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0" style="position: relative">
    <img src="/img/static/logmeonce.png" style="height: 356px;" class="img-fluid w-100" alt="">
    <div class="overlay"></div>
</section>
<section class="bg-white" style="height: 700px; width: 100%"></section>
<div class="left_sidebar left_middle">
    <p class="scrolltotop"><i class="fas fa-arrow-up"></i></p>
    <p> <a href="{{ route('index') }}"><i class="fas fa-arrow-left"></i></a></p>
    <p class="custom_writing_text">Product Design</p>
</div>
<div class="left_sidebar">
    <p><i class="fas fa-arrow-up"></i></p>
    <p><i class="fas fa-arrow-left"></i></p>
    <p class="custom_writing_text">photography</p>
</div>
<div class="right_sidebar right_middle text-end">
    <p class="text-start text-dark right_option fw-bold">Introduction<span>
        <i class="fas fa-circle text-white custom_circle_icon ps-2" id="circle_black"></i>
    </span></p>
    <p class="text-start right_option text-dark fw-bold">Research<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span>
    </p>
    <p class="text-start right_option text-dark fw-bold">Design<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span>
    </p>
    <p class="text-start  right_option text-dark fw-bold">Testing<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i>
    </span></p>
    <p class="text-start right_option text-dark fw-bold">Product<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i>
    </span></p>
    <p class="text-start right_option text-dark fw-bold">Reflection<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i>
    </span></p>
</div>


@endsection

@section('scripts')
<script src="{{ asset('scripts/script.js') }}"></script>
@endsection
