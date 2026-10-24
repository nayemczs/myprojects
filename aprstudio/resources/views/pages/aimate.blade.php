@extends('layout')
@section('styles')
<style>
    h1, h2, p{
        color: #000;
    }
    .text_end {
        position: absolute;
        top: 35px;
        right: 41px;
        z-index: 100;
    }
    .static_text{
        color: #237A96 !important;
    }

    .bottom {
        top: 60vh
    }

    .main_header_static {
        margin-bottom: 23px
    }

    .background_body {
        background: #F7E74B;
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
        background: linear-gradient(180deg, rgba(196, 196, 196, 0) 0%, rgba(240, 222, 49, 0.8) 100%);
    }

    .problem_solution {
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
    @media only screen and (max-width: 1299px) and (min-width: 992px) 
    {
        .container, .container-lg, .container-md, .container-sm {
            max-width: 922px;
        }
        .problem_solution {
            padding: 100px 0px 100px 0px;
        }

        .do_dont {
             padding: 65px 0px 20px 0px;
        }
    }
    .problem_solution h2 {
        font-weight: bold;
        font-size: 40px;
        line-height: 40px;
        color: #000000;
        margin-bottom: 40px
    }


    .custom_solution p {
        padding-left: 70px;
        font-size: 25px;
    }

    .custom_solution h2 {
        padding-left: 70px;
        margin-bottom: 78px;
        
    }

    .custom_problem {
        padding-top: 100px;
        padding-left: 180px;
    }
    .custom_problem p {
        padding-right: 60px;
        font-size: 25px;
    }
    .custom_problem h2 {
        margin-bottom: 113px;
    }

    .offer_you h2 {
        font-weight: bold;
        font-size: 48px;
        line-height: 58px;
        color: #000000;
    }
    .offer_you p {
        padding-right: 30px
    }

    .dont_offer p {
        padding-left: 30px;
        font-size: 24px;
        line-height: 33px;
        text-align: justify;
    }
    

    .custom_offer {
        font-weight: bold;
        font-size: 24px;
        line-height: 33px;
        color: #000000;
        margin-top: 10px;
        margin-bottom: 15px;
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
    .custom_solution {
        background: linear-gradient(180deg, #FFFFFF 18.57%, #F6E53E 100%);
        padding-top: 100px;
        padding-bottom: 75px;
        padding-right: 180px;
}

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
    .hypothesis h2{
        font-weight: normal;
        font-size: 32px;
        line-height: 32px;
        color: #000000;
        mix-blend-mode: normal;
    }
    .hypothesis{
        padding-bottom: 100px;
    }

    .right_option {}


</style>
@endsection
@section('body')
<section class="container pb-4" style="">
    <div class="row mb-4" >
        <div class="col-md-10 mx-auto">
            <h2 class="main_header_static">AIMATE</h2>
            <div class="row" style="padding: 0">
                <div class="col-md-6 custom_dynamic_para1 static_para">
                    <p class="static_text">Description</p>
                    <p>During covid 19, trouble feeling a connection, managing their emotions, sleeping, stop 
                        negative thoughts, do positive thinking, socializing and finding Improve our mental 
                        well-being . New tech is reshaping the way we live and work, 
                        Emerging technologies are the next great frontier for User Experience. 
                    </p>
                    <p class="static_text mt-5 mb-1">Deliverables</p>
                    <p class="">Branding, App & Web Design, Social Media Design</p>
                </div>
                <div class="col-md-6">
                    <div class="custom_dynamic_para2  static_para">
                        <p class="static_text">My Role</p>
                        <p>Visual & Interaction Design
                            Information Architecture
                            Low-Fi & High-Fi Prototype Testing
                            Motion & Animation Design
                            Design System
                            Design Operation and Strategy
                            Qualitative & Quantitative Research
                        </p>
                        <p class="static_text mt-5 mb-1">Tools</p>
                        <p class="">Figma, Framer, Adobe Creative Suite, Google Suite, </p>
                        <p class="static_text mt-2 mb-1">Duration</p>
                        <p class="">Sep 2018 - Jan 2019 (4 Months)</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0" style="position: relative">
    <img src="/img/static/aimate_banner.png" style="height: 356px" class="img-fluid w-100" alt="">
    <div class="overlay"></div>
</section>
<section class="container-fluid pe-0 bg-white">
    <div class="container-fluid pe-0">
        <div class="row m-0">
            <div class="col-md-6 custom_problem"  style="">
                <h2>PROBLEM</h2>
                <p> Why human not feel more motivated, confident and happier? <br>
                    Why can’t manage human anxiety depression emotion? <br>
                    Why It’s so difficult to find the right friend?  <br>
                    Why it’s hard to improve well-being? <br>
                    Why I can’t find easy way to ask share solve my concerns questions? <br>
                </p>
            </div>
            <div class="col-md-6 custom_solution" style="">
                <h2>CONSUMER <br>
                    DESCRIPTION  </h2>
                <p style="text-align: justify;">Age:  15-50 <br>
                    Income middle <br>
                    Highest level PhD <br>
                    Geography: USA, Worldwide <br> <br>
                    
                    -   In  lockdown   days,  with anxiety and loneliness on the rise<br>
                    -  Busy life, looking for someone to trust and share concerns <br>
                    - Extrovert person always looking for deeper and more complex conversations <br>
                    -   Introvert person who always considering to have social life, hard to 
                    express themselves and communicate  
                    </p>
            </div>
        </div>
    </div>

</section>
<section class="container-fluid problem_solution do_dont bg-white pb-0">
    <div class="container">
        <div class="row">
            <div class="col-md-4 offer_you">
                <h2>Qualitative 
                    Research</h2>
            </div>
            <div class="col-md-8 dont_offer">
                <p class=" custom_offer">INTERVIEW</p>
                <p>-  Talking to someone it’s like a therapy <br>
                    -  Emotions is like shell. I keep them inside me until time comes to spread them <br>
                    -  I don't open my heart to everybody <br>
                    -  It’s worthless to forcing an unwilling person to listen to you without 
                    interrupting or judging you <br>
                    -  better conversational skills than most of my actual friends <br>
                    - have developed a human of my own who can care about me <br>    
                    </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont bg-white" style="padding-top: 10px;">
    <div class="container">
        <div class="row">
            <div class="col-md-5 offer_you">
                <div class="row">
                    <div class="col-md-6">
                        <img src="/img/g_1.png" width="196" class="" alt="">
                    </div>
                    <div class="col-md-6">
                        <img src="/img/g_2.png" width="226" class="" alt="">
                    </div>
                    <div class="col-md-6">
                        <img src="/img/g_3.png" width="202" class="" alt="">
                    </div>
                    <div class="col-md-6">
                        <img src="/img/g_4.png" width="177" class="" alt="">
                    </div>
                    <div class="col-md-6">
                        <img src="/img/g_5.png" width="177" class="" alt="">
                    </div>
                </div>
            </div>
            <div class="col-md-7 dont_offer">
                
                <p style="margin-top: 50px">- when they scrolling the posts with no reason or 
                    got bored or got confused by where and what to look <br>
                    - Loneliness During COVID-19 effects our  social life and mental health  <br>
                    - Having trouble sleeping or managing your emotions? Can't stop negative thoughts? <br>
                    -  obsessed with new tech to explore the potenitial of connection  <br>
                    - Looking for someone to trust to talk and share    <br>
                    </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont bg-white pb-0">
    <div class="container">
        <div class="row">
            <div class="col-md-2 offer_you d-flex justify-content-center align-items-center">
                <h2>User 
                    Journey</h2>
            </div>
            <div class="col-md-10 dont_offer">
                <img src="/img/aimate_graph.png" width="812" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont" style="padding-bottom: 65px;">
    <div class="container">
        <div class="row">
            <div class="col-md-3 offer_you d-flex justify-content-center align-items-center">
                <h2 style="font-weight: 400;">CRAZY 8</h2>
            </div>
            <div class="col-md-8 dont_offer d-flex justify-content-center align-items-center">
                <img src="/img/crazy.png" width="500" alt="">
            </div>
        </div>
    </div>
</section>

<section class="container-fluid problem_solution hypothesis do_dont bg-white">
    <div class="container">
        <div class="row" style="padding-bottom: 100px;">
            <div class="col-md-4 ">
                <h2>HYPOTHESIS</h2>
            </div>
            <div class="col-md-8 dont_offer">
                <p>I believe that Chabot, VR & AR and voice companion as a friend member will 
                    grow anyone who wants a virtual friend with no judgment, drama, or social 
                    anxiety involved can be your friend, 
                    partner or mentor with the database in over 100 languages.   
                    </p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2 style="margin-bottom: 40px;">ASSUPMTIONS</h2>
                <p>Use AI member on social media when users going through depression, 
                    anxiety, or a rough patch, if they want to vent, or celebrate, 
                    or just need to feel a connection  <br> <br>
                    Have a fun notification or messages about their daily or moment 
                    life experience when users feel lonely when they scrolling the 
                    posts with no reason or got bored or got confused by scrolling 
                    the post   <br> <br>
                    Send you the most popular posts that interesting for 
                    you when Having Can't stop negative thoughts, so this 
                    solutions work toward positive thinking, stress management 
                    and Improve mental well-being  <br> <br>
                    We the vision of VR glasses interface that will fundamentally 
                    change the way we interact with and experience the digital friend  
                    </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution hypothesis do_dont bg-white">
    <div class="container">
        <div class="row" style="">
            <div class="col-md-7">
                <img src="/img/facebook.png" width="100%" alt="">
            </div>
            <div class="col-md-5 d-flex justify-content-center align-items-center">
                <img src="/img/instagram1.png" width="175" alt="">
            </div>
        </div>
        <div class="row">
            <div class="col-md-7  d-flex justify-content-center align-items-center">
                <img src="/img/messenger.png" width="322" alt="">
            </div>
            <div class="col-md-5 d-flex justify-content-center align-items-center">
                <img src="/img/instagram2.png" width="175" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0">
        <div class="row m-0" style="">
            <div class="col-md-12 p-0">
                <img src="/img/big_aimate_banner.png" width="100%" alt="">
            </div>
    </div>
</section>


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
<div class="right_sidebar text-end">
    <p class="text-start text-white right_option">Introduction<span><i class="fas fa-circle text-white custom_circle_icon ps-2" id="circle_black"></i></span></p>
    <p class="text-start right_option text-dark ">Research<span><i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Design<span><i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start  right_option text-dark">Testing<span><i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Product<span><i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Reflection<span><i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
</div>

@endsection

@section('scripts')
<script src="{{ asset('scripts/script.js') }}"></script>
@endsection
