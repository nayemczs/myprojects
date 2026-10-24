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
        background-color: #A4BFF4;
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
        background: linear-gradient(180deg, rgba(196, 196, 196, 0) 0%, rgba(164, 191, 244, 0.8) 70.83%);
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
    <div class="row mb-4" >
        <div class="col-md-10 mx-auto">
            <h2 class="main_header_static">BEGOOD</h2>
            <div class="row" style="padding: 0">
                <div class="col-md-6 custom_dynamic_para1 static_para">
                    <p class="static_text text-white">Description</p>
                    <p>We want to be well informed but it is taking a toll on our well-being.
                        Disaster news is the number one category in the news interest index
                        and there are studies proving that exposure to bad news can cause
                        anxiety, mood disorders and can even be addictive. There are reasons
                        why news is bad for us: It disrupts our thinking, it changes our brain,
                        it’s stressful .
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
                        <p class="">Nov 2019 - June 2020 (8 Months)</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0" style="position: relative">
    <img src="/img/static/static_banner.png" style="height: 356px" class="img-fluid w-100" alt="">
    <div class="overlay"></div>
</section>
<section class="container-fluid problem_solution">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_problem">
                <h2>PROBLEM</h2>
                <p>A Collection of Motivational Podcasts and Videos from Inspiring Speakers
                    Support a charity with every purchase, get a GNN discount on every product 
                    Offers daily updates of “good news” events from around the world </p>
            </div>
            <div class="col-md-6 custom_solution">
                <h2>SOLUTION</h2>
                <p>A Collection of Motivational Podcasts and Videos from Inspiring Speakers
                    Support a charity with every purchase, get a GNN discount on every product 
                    Offers daily updates of “good news” events from around the world </p>
            </div>
        </div>
    </div>

</section>
<section class="container-fluid problem_solution do_dont bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_problem offer_you">
                <h2>Direct Competitors</h2>
                <img src="/img/static/goodnews.png" alt="good news">
                <p>The good news network delivers daily positive news from around the world.
                    Trusted by millions of readers for almost two decades.
                    It’s number one on google for good news.
                </p>
            </div>
            <div class="col-md-6 custom_solution dont_offer">
                <p class=" custom_offer"> What the app does offer</p>
                <p>A Collection of Motivational Podcasts and Videos from Inspiring Speakers
                    Support a charity with every purchase, get a GNN discount on every product 
                    Offers daily updates of “good news” events from around the world </p>
                <p class=" custom_offer mt-4">WHAT THE APP DOESN’T OFFER </p>
                <p>Can’t organize, read and share what matters to you
                    Can’t customize your interest and can’t Keep up with all the topics that matter to you 
                    Can’t Discover and share the stories that does matter for you and shape your world</p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution related_web bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_problem offer_you">
                <img class="" src="/img/static/media.png" alt="good news">
            </div>
            <div class="col-md-6 custom_solution dont_offer">
                <p class=" custom_offer">HOW CAN THIS WEB APP RELATE TO MY WEB APP</p>
                <p>read the news and information you need to stay positive
                    Don't miss a beat from New York Times or any other industry journal you trust
                    Let the web work for you by arranging the content you rely on into easy-to-read category
                </p>
            </div>
        </div>
    </div>

</section>
<section class="container-fluid problem_solution related_web bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_problem offer_you">
                <h2>Indirect Competitors</h2>
                <img class="" src="/img/static/inform.png" alt="good news">
            </div>
            <div class="col-md-6 custom_solution dont_offer">
                <p><strong>FLipboard</strong> aggregates content from social media,
                    news feeds, photo sharing sites and other websites, presents it in magazine
                    format, and allows users to "flip" through the articles, images and videos
                    being shared. Readers can also save stories into Flipboard magazines.
                </p>
                <p class="custom_offer">HOW CAN THIS WEB APP RELATE TO MY WEB APP</p>
                <p>Bringing together your favorite news sources with social content, from
                    political issues to technology trends to travel inspiration
                    Beople can find quality stories on any interest, investing in their lives and their passions
                </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution custom_research">
    <div class="container">
        <div class="row">
            <div class="col-md-3 custom_problem offer_you d-flex justify-content-center align-items-center">
                <h2>Qualitative <br>
                    Research</h2>
            </div>
            <div class="col-md-9 custom_solution dont_offer">
                <p class="custom_offer">After learning about how is plogging done,
                    I <strong>surveyed</strong> and <strong>interviewed</strong> with people to
                    <strong>undersand</strong> user’s motivations and identify their needs
                </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution interview bg-white">
    <div class="container">
        <h2>INSIGHT OF <br>
            INTERVIEW</h2>
        <div class="row">
            <div class="col-md-3 d-flex justify-content-center align-items-center">
                <img src="/img/static/man_with_sunglass.png" alt="good news">
            </div>
            <div class="col-md-3">
                <p>They know people’s need, what they would love to hear on social media,
                    and they would highlight that theme.
                    “I basically got tired of hearing negative news stories“</p>
            </div>
            <div class="col-md-3  d-flex justify-content-center align-items-center">
                <img src="/img/static/a_man.png" alt="good news">
            </div>
            <div class="col-md-3">
                <p>conversation through important and influential stories that not only
                    keep people informed, but also inspire them to engage, learn and lead
                    “negative news causes my mind and body to go into overdrive as they
                    continuously focus on what might happen“</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-5">
                <h2 class="mb-0">SURVEY</h2>
                <p class="fw-bold mb-0">PARTISIPANTS : 28 </p>
                <p class="fw-bold mb-0">RESPONSED : 10</p>
                <img src="/img/static/1st_chart.png" class="mt-4 img-fluid" alt="">
            </div>
            <div class="col-md-7">
                <img src="/img/static/2nd_chart.png" class="mt-4 img-fluid" alt="">
            </div>

        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont interview bg-white">
    <div class="container">
        <h2>Personas</h2>
        <div class="row my-5">
            <div class="col-md-3">
                <img src="/img/static/sunglass_man.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-3 custom_personas">
                <p class="fw-bold">
                    Demographis
                </p>
                <p class="mb-0">
                    Name: Ramy <br>
                    Age: 32 <br>
                    Status: Single <br>
                    Job: Artist <br>
                    Education: MA <br>
                    Location: New York <br>
                    Passions: <br>
                    Art, Travelling, Hicking Income: 50K
                </p>
            </div>
            <div class="col-md-3 custom_personas">
                <p class="fw-bold">
                    Background
                </p>
                <p class="mb-0">
                    I'm multi-disciplinary Artist, his research tracks the functional ity of crafted objects
                    and the stories behind cultural ornamen tation.
                    I would like change myself with new ideas and combine Design and Technology
                </p>
            </div>
            <div class="col-md-3 custom_personas">
                <p class="fw-bold">
                    Pschographics
                </p>
                <p class="mb-0">
                    <strong>Attitude:</strong> I am a moody person, I'm a bit of an introvert.
                    <br>
                    <br>
                    <strong>Values:</strong> high levels of effort and motivation, work well in team settings, excitable, often very dynamic
                </p>
            </div>
        </div>
        <div class="row my-5">
            <div class="col-md-3">
                <img src="/img/static/a-man_saquare.png" class="img-fluid w-100" alt="">
            </div>
            <div class="col-md-3 custom_personas">
                <p class="mb-0">
                    Name: Foad<br>
                    Age: 55 <br>
                    Status: Married <br>
                    Job: Doctor <br>
                    Education: Phd <br>
                    Location: New York <br>
                    Passions: <br>
                    Technology, medicine, Art, <br>
                    Income: 200K
                </p>
            </div>
            <div class="col-md-3 custom_personas">
                <p class="mb-0">
                    I am director of Istaton Island Hospital. I'm always planning to change my enviromnet,.
                    Focus on Migration, Climate change, Lack of Ecucation, Enviromental issues.
                    I would like to find inter esting program to have the students participate in for sus tainability.
                </p>
            </div>
            <div class="col-md-3 custom_personas">
                <p class="mb-0">
                    <strong>Attitude:</strong> I would describe myself as bubbly and very nice,try to be very social, Helpful
                    <br>
                    <br>
                    <strong>Values:</strong> I am independent and determined, extremely sensi tive and an over thinker
                </p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution custom_research bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-4 custom_problem offer_you">
                <p class="logo_edit">Logo</p>
                <p class="color_edit">Colors</p>
                <p>Primary Font</p>
            </div>
            <div class="col-md-8 custom_solution dont_offer">
                <img src="/img/static/logos_icons.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution custom_research bg-white pt-0">
    <div class="container">
        <div class="row">
            <div class="col-md-12 custom_solution dont_offer">
                <img src="/img/static/image15.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution custom_flow  pt-0">
    <div class="container">
        <div class="row">
            <div class="col-md-2 dont_offer">
                <h2>USER FLOW</h2>
            </div>
            <div class="col-md-2 custom_solution dont_offer flow_btns">
                <button class="common_btn">HOME PAGE</button>
                <button class="common_btn btn_eclipse">Login</button>
                <button class="common_btn btn_eclipse">Guest</button>
                <button class="common_btn btn_eclipse">Sign Up</button>
            </div>
            <div class="col-md-2 custom_solution dont_offer flow_btns">
                <button class="common_btn btn_third">Dashbo</button>
                <button class="common_btn btn_third">Discov</button>
                <button class="common_btn btn_third">Crea</button>
                <button class="common_btn btn_third">Conta</button>
                <button class="common_btn btn_third">Shar</button>
                <button class="common_btn btn_third">Calend</button>
                <button class="common_btn btn_third">Remind</button>
            </div>
            <div class="col-md-2 custom_solution dont_offer flow_btns">
                <button class="common_btn btn_four">Messages</button>
                <button class="common_btn btn_four">Interest</button>
                <button class="common_btn btn_four">Local</button>
                <button class="common_btn btn_four">My Page</button>
                <button class="common_btn btn_four">List</button>
                <button class="common_btn btn_four">Performance</button>
                <button class="common_btn btn_four">To Do</button>
            </div>
            <div class="col-md-2 custom_solution dont_offer flow_btns">
                <button class="common_btn btn_five">Calender</button>
                <button class="common_btn btn_five">List</button>
                <button class="common_btn btn_five">International</button>
                <button class="common_btn btn_five">List</button>
                <button class="common_btn btn_five">Edit</button>
            </div>
            <div class="col-md-2 custom_solution dont_offer flow_btns">
                <button class="common_btn btn_six">Read News</button>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0">
    <img src="/img/static/blue_banner.png" class="img-fluid w-100" alt="">
</section>
<section class="container-fluid problem_solution custom_footer bg-white pt-0">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_solution dont_offer">
                <img style="margin-top: 150px; margin-bottom: 25px" src="/img/static/footer_1.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-6 custom_solution dont_offer">
                <img style="margin-top: 150px; margin-bottom: 25px" src="/img/static/footer_2.png" class="img-fluid" alt="">
            </div>
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
