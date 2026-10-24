@extends('layout')
@section('styles')
<style>
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
        margin-bottom: 23px;
        font-size: 48px;
        color: #000;
    }

    .background_body {
        background-color: #F9F5E6;
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
        background: linear-gradient(180deg, rgba(196, 196, 196, 0) 0%, rgba(249, 245, 230, 0.8) 70.83%);

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
    .problem_text{
        margin-bottom: 30px;
    }
    .custom_museum_details{
        display: flex;
        flex-direction: column;
        margin-left: 10px;
        justify-content: center;
    }
    .custom_discuss{
        margin-top: 103px;
        margin-bottom: 73px;
    }
    .custom_brand {
        font-size: 25px;
        line-height: 65px;
        text-align: center;
        width: 375px;
        padding: 10px 10px;
        border-bottom: 1px solid black;
        color: #000000;
        display: inline-block
    }
    .custom_news{
        position: relative;
        height: 1000px;
        margin-bottom: -78px;
    }
    .news_one {
        width: 649px;
        position: absolute;
        left: 0;
        z-index: 9;
        top: 0;
    }
    .news_two {
        width: 595px;
        position: absolute;
        bottom: 90px;
        right: 0px;
    }
    .custom_three{
        display: flex;
        justify-content: center
    }
    
    .custom_single {
        background-color: #F6F6F6;
        display: flex;
        justify-content: center;
    }
    .custom_single_two{
        font-weight: 500;
    }
    .custom_silver {
        font-size: 8px;
    }
    .custom_single_two p{
        color: #000;
        line-height: 32px;
        font-weight: 500;
    }
    .custom_upper{
        text-transform: uppercase;
        line-height: 22px;
        color: black;
        font-weight: 500;
    }
    .custom_light {
        border: 1px solid #000000;
        box-sizing: border-box;
        width: 75px;
        margin-right: 13px;
        text-align: center;
        
    }
    .big_letter{
        font-size: 18px; 
        letter-spacing: 0.2em;
    }
    .small_letter {
            text-transform: lowercase;
             letter-spacing: 0.2em;
        }
    @media only screen and (max-width: 1299px) and (min-width: 992px) 
    {
        .problem_solution h2 {
            font-size: 24px;
        }
        .big_letter{
            font-size: 14px; 
            letter-spacing: 0em;
        }
        .small_letter {
            letter-spacing: 0em;
        }

    }
    .right_option {}


</style>
@endsection
@section('body')
<section class="container pb-4" style="">
    <div class="row">
        <div class="col-md-10 mx-auto">
            <h2 class="main_header_static">NATURAL MUSEUM OF HISTORY</h2>
            <div class="row" style="padding: 0">
                <div class="col-md-6 custom_dynamic_para1 static_para">
                    <p class="static_text">Description</p>
                    <p>The goal of any museum is to preserve its collection and modernize its presentation, 
                        in order to preserve unique monuments and civilizational wealth for the coming generations 
                        and, at the same time, to encourage the interest of potential visitors. Museum web- sites 
                        “significant means for reaching vast audiences and 
                        which serve to inform, educate, and encourage online visitors to participate in museum life .
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
                        <p class="">Apr 2017 - Jul 2017 (3 Months)</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid p-0" style="position: relative">
    <img src="/img/static/natural2.png" style="height: 356px;" class="img-fluid w-100" alt="">
    <div class="overlay"></div>
</section>
<section class="container-fluid problem_solution">
    <div class="container">
        <div class="row">
            <div class="col-md-10 custom_problem d-flex ">
                <img src="/img/static/natural_problem.png" width="273"  alt="">
                <div class="custom_museum_details">
                    <p class="static_text problem_text">Problem</p>
                    <p>Museums should turn to marketing in order to increase audiences, 
                        embrace the latest technology in communication with the market. 
                    </p>
                </div>
            </div>
        </div>
        <div class="row justify-content-end mt-4">
            <div class="col-md-10 custom_problem d-flex ">
                <img src="/img/static/natural_target.png" width="273"  alt="">
                <div class="custom_museum_details">
                    <p class="static_text problem_text">Target</p>
                    <p>To turn non visitors into visitors, visitors into repeat 
                        visitors and regular museum goers into supporters 
                    </p>
                </div>
            </div>
        </div>
        <div class="row justify-content-center mt-4">
            <div class="col-md-6 custom_problem d-flex ">
                <div class="custom_museum_details">
                    <p class="static_text problem_text ms-0">Solution</p>
                    <p>Museums should turn to marketing in order to increase audiences, 
                        embrace the latest technology in communication with the market. 
                        
                    </p>
                </div>
            </div>
        </div>
   
    <div class="row justify-content-center mt-4">
        <div class="col-md-12 custom_problem d-flex ">
            <img src="/img/static/natural.png" class="img-fluid"  alt="">

        </div>
    </div>
</div>
</section>
<section class="container-fluid bg-white ">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-10 custom_problem d-flex justify-content-end my-4">
                <p>Goal: visualize for every visitor <br> from beginning to end</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12 custom_problem d-flex justify-content-center mb-4">
                <img src="/img/static/natural_graph.png" class="img-fluid"  alt="">
            </div>
        </div>

    </div>

</section>

<section class="container-fluid problem_solution do_dont">
    <div class="container">
        <div class="row">
            <div class="col-md-4 custom_problem offer_you">
                <h2 class="" style="">INSIGHT OF INTERVIEW</h2>
                <div class="" style="border-right: 9px solid #000; margin-top: 130px">
                    <img src="/img/static/discuss.png" alt="lets discuss" class="img-fluid custom_discuss">
                </div>
            

            </div>
            <div class="col-md-8 custom_solution">
                <div>
                    <img src="/img/static/green.png" alt="lets discuss" style="height: 275px" class="img-fluid my-1">
                </div>
                <div>
                    <img src="/img/static/red.png" alt="lets discuss" style="height: 275px" class="img-fluid my-2">
                </div>
                <div>
                    <img src="/img/static/blue.png" alt="lets discuss" style="height: 275px" class="img-fluid my-1">
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont">
    <div class="container">
        <div class="row">
            <div class="col-md-4 custom_problem offer_you">
                <h2 class="" style="">BRAND <br> TRAITS</h2>
            </div>
            <div class="col-md-5">
                <div class="text-center my-4">
                    <p class="custom_brand">Modern but not Traditional</p>
                    <p class="custom_brand">Creative but not Down to earth </p>
                    <p class="custom_brand">Broad minded but not Distant </p>
                    <p class="custom_brand">Scientific but not Academical</p> <br>
                    <p class="custom_brand">Encoraging but not Boring </p>
                </div>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont">
    <div class="container">
        <div class="row">
            <div class="col-md-2 custom_problem offer_you">
                <h2 class="" style="">COLOR <br> PALETTE</h2>
            </div>
            <div class="col-md-9">
                <img src="/img/static/tea.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid  bg-white" style="    padding: 80px 180px 80px 180px;">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_single_two">
                <p style="font-weight: bold;">TYPOGRAPHY</p>
                <p style="font-weight: bold;">TYPeface</p>
                <p style="" class="big_letter">ABCDEFGHIGKLMNOPQRSTUVWXYZ</p>
                <p class="small_letter" style="">ABCDEFGHIGKLMNOPQRSTUVWXYZ</p>
                <p style="font-size: 18px; letter-spacing: 0.2em;">0123456789</p>
                <p style="font-size:20px; margin-top: 30px; font-weight: bold;">FONT WEIGHT</p>
                <div class="d-flex mt-3">
                    <div class="custom_light">
                        <p style="margin-bottom: 4px; font-weight: light;">Aa</p>
                        <p>Light</p>
                    </div>
                    <div class="custom_light">
                        <p style="margin-bottom: 4px; font-weight: 600;">Aa</p>
                        <p>Medium</p>
                    </div>
                    <div class="custom_light">
                        <p style="margin-bottom: 4px; font-weight: 900;">Aa</p>
                        <p>Bold</p>
                    </div>
                </div>

            </div>
            <div class="col-md-6">
                <p class="custom_upper mb-3" style="font-size: 20px">FONT SIZE</p>
                <p class="custom_upper" style="font-size: 18px;">a leader in the natural sciences.</p>
                <p class="custom_upper custom_silver">18px - extra large</p>
                <p class="custom_upper" style="font-size: 15px;">a leader in the natural sciences. </p>
                <p class="custom_upper custom_silver ">15px - extra large</p>
                <p class="custom_upper" style="font-size: 11px;">a leader in the natural sciences. </p>
                <p class="custom_upper custom_silver">11px - extra large </p>
                <p class="custom_upper" style="font-size: 8px;">a leader in the natural sciences. </p>
                <p class="custom_upper custom_silver">8px - extra large</p>
            </div>
        </div>
    </div>
</section>
<section class="container-fluid">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-7">
                <img src="/img/static/info.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-3 custom_problem offer_you">
                <h2 class="" style="">SKETCH</h2>
            </div>
            <div class="col-md-9 mt-3">
                <img src="/img/static/sketch_one.png" class="img-fluid" alt="">
                <img src="/img/static/sketch_two.png" class="img-fluid mt-3" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont bg-white">
    <div class="container">
        <div class="row">
            <div class="col-md-3 custom_problem offer_you">
                <h2 class="" style="">WIREFRAMES</h2>
            </div>
            <div class="col-md-9">
                <img src="/img/static/wireframes.png" class="img-fluid" alt="">
            </div>
        </div>
    </div>
</section>
<section class="container-fluid py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-12 justify-content-center">
                <div class="custom_news">
                    <div class="news_one">
                        <img src="/img/static/big_one.png" width="649" style="border: 2px solid black;" class="img-fluid" alt="">
                    </div>
                    <div class="news_two">
                        <img src="/img/static/big_two.png" width="595" class="img-fluid" alt="">
                    </div>
                   
                </div>
                
            </div>
        </div>
    </div>
</section>
<section class="container-fluid problem_solution do_dont" style="padding-bottom: 100px;">
    <div class="container">
        <div class="row">
            <div class="col-md-6 custom_single">
                <img src="/img/static/natural_single.png"  alt="">
            </div>
            <div class="col-md-6">
                <img src="/img/static/natural_single_two.png" class="img-fluid" width="451" alt="">
            </div>
            <div class="col-md-6 custom_three">
                <img src="/img/static/natural_single_three.png" class="img-fluid" alt="">
            </div>
            <div class="col-md-6">
                <img src="/img/static/natural_single_four.png" class="img-fluid" width="451" alt="">
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
<div class="right_sidebar middle_one text-end">
    <p class="text-start right_option"><a href=""> Introduction<span>
        <i class="fas fa-circle custom_circle_icon ps-2" id="circle_black"></i></span></a></p>
    <p class="text-start right_option text-dark ">Research<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Design<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start  right_option text-dark">Testing<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Product<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
    <p class="text-start right_option text-dark ">Reflection<span>
        <i class="fas fa-circle custom_circle_icon  ps-2" id="circle_silver"></i></span></p>
</div>

@endsection

@section('scripts')
<script src="{{ asset('scripts/script.js') }}"></script>
@endsection
