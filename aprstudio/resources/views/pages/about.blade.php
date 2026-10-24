@extends('layout')
@section('styles')
<link href="https://fonts.googleapis.com/css2?family=Blinker&display=swap" rel="stylesheet">
<style>

    .background_body {
        font-family: 'Blinker', sans-serif !important;
        padding-bottom: 50px
    }
    h5, p, a {
        font-family: 'Blinker', sans-serif !important;
    }
    .custom_contact_header {
        font-size: 75px;
        margin-left: 100px;
        line-height: 85px;
        font-weight: 400;
    }

    .custom_contact_text {
        color: lightgray;
        font-size: 26px;
    }

    .custom_contact_location {
        font-size: 20px;
    }
    hr {
        height: 3px !important;
        background-color: white;
        width: 50px;
    }
    p {
        margin-bottom: 0px
    }
    .about_left_header{
        position: relative;
        width: 239px;
        height: 299px;
        background: #C4C4C4;
        border-radius: 105px;
    }
    .about_overlay {
        position: absolute;
        width: 239px;
        height: 238px;
        left: 0px;
        top: 62px;
        background: linear-gradient(180deg, rgba(227, 84, 64, 0) 22.05%, rgba(227, 84, 64, 0.85) 94.56%);
        border-radius: 105px;
    }
    .about_left, .about_content{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .about_square{
        height: 62.5px;
        position: absolute;
        bottom: -25px;
    }
    .about_content_main {
        font-family: Abhaya Libre ExtraBold;
        font-weight: 800;
        font-size: 36px;
        line-height: 42px;
        color: #000000;
        width: 134px;
    }
    .about_submain {
        font-weight: 500;
        font-size: 18px;
        line-height: 25px;
        color: #000000;
        margin-top: 25px;
    }
    .about_ul {
        margin-left: 39px;
        margin-bottom: 5px;
        padding-left: 0px;
    }
    .about_ul li {
        list-style: none;
        font-family: Avenir Next;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 39.7px;
        /* or 158% */

        letter-spacing: 0.01em;

        color: #000000;
    }
    .right_one p {
        font-weight: bold;
        font-size: 20px;
        line-height: 22px;
        width: 86px;
        text-align: right;
        color: #000000;
        line-height: 38px;
    }
</style>
@endsection
@section('body')
<section class="container py-4 px-4" style="">
    <div class="row">
        <div class="col-lg-4 col-12">
            <div class="about_left">
                <div class="about_left_header mb-5">
                    <div class="about_overlay">
                        <div class="about_square">
                            <img src="/img/square.svg" width="80" alt="">
                        </div>
                    </div>
                </div>
                <div class="about_content">
                    <p class="about_content_main text-left">HI,</p>
                    <p class="about_content_main text-center">I’m Ali</p>
                    <p class="about_submain">I am passionate about using qualitative and quantitative data to 
                        deliver novel insights for product research and business processes  
                        I leverage my role as a design thinker to reimagine the human-aspects 
                        of our technologies, through UX/product design & research. 
                    </p>
                </div>
            </div>
        </div>
        <div class="col-lg-8 col-12">
            <div class="right_one">
                <p>Education</p>  
                <ul class="about_ul">
                   
                    <li>-  &nbsp;&nbsp; 
                        Master of Art Web and Multimedia Design / Touro College / NYC / 2019
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Bachelor Of Fine Art / Visual Communication Design / TCA / 2011
                    </li>
                </ul>
                <p>CERTIFICATES</p>
                <ul class="about_ul">
                    <li>-  &nbsp;&nbsp; 
                        Product Designer ( UX & UI )/ Logmeonce / NYC / 2020 - Present
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        led the design vision and helped to set the product direction and build and test of feautures.
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Facilitated the client’s product vision rapidly by researching, conceiving, sketching, prototyping,
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        UX/UI Designer, Front end developer/ Freelance / NYC / 2014 - Present
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Worked directly with clients, stakeholders, and engineers on multiple projects
                    </li>
                </ul>
                <p>EMPLOYMENT</p>
                <ul class="about_ul">
                    <li>-  &nbsp;&nbsp; 
                        UX/UI Designer / Pixel One / NYC / 2017 - 2018
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Colaberate with the research, design, prototyping, testing, and development to improve UX/UI
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        UX/UI Designer, Front end developer Samsonic / NYC / 2016 - 2017
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Art Director / Simagohar / 2006 - Presentlead and design the branding
                    </li>
                    <li>-  &nbsp;&nbsp; 
                        Website, packaging, retail displays, apps and all touch points for the brand.

                    </li>
                </ul>
{{-- 
<li>-  &nbsp;&nbsp; 
    Graphic/Web Designer / At Personal Studio ( Pyramid Studio ) / 2009 - Present

</li>
<li>-  &nbsp;&nbsp; 
    Worked directly with clients, stakeholders, and engineers on multiple projects

</li>
<li>-  &nbsp;&nbsp; 
    Graphic Designer / Toranj Studio / 2007-2008

</li>


<li>-  &nbsp;&nbsp; 
    Designed graphics and user interfaces for various brands
</li>
<li>-  &nbsp;&nbsp; 
    Digital Product Design / Pratt School / NYC / 2019
</li>
<li>-  &nbsp;&nbsp; 
    Human-Computer Interaction / Massachusetts Institute of Technology / MIT / 2019
</li>
<li>-  &nbsp;&nbsp; 
    UX Certified / NN/g / Nielson Norman Group / NYC / 2019
</li>
<li>-  &nbsp;&nbsp; 
    Interaction Deisgn / School of Visual Deisgn / NYC / 2019
</li>
<li>-  &nbsp;&nbsp; 
    Diploma User Experience Design / New York University / NYC / 2017
</li>
<li>-  &nbsp;&nbsp; 
    Diploma Digital Marketing / New York University / NYC / 2017
</li>
<li>-  &nbsp;&nbsp; 
    Product Management Bootcamp / Product School / NYC / 2019
</li>




<li>-  &nbsp;&nbsp; 
    Full Stack Product Managment Certificate / Product School / NYC / 2020
</li>
<li>-  &nbsp;&nbsp; 
    Interaction Design, Interface Deisgn, Information Architecture, Sketching,
</li>
<li>-  &nbsp;&nbsp; 
    Storyboarding, User Flows, Wireframing, Prototyping, Mockups, Responsive design
</li>
<li>-  &nbsp;&nbsp; 
    Inclusive Design
</li>
<li>-  &nbsp;&nbsp; 
    Focus Groups, Observation, Design Evaluation, Ethnographic Research, Task Analysis,
</li>
<li>-  &nbsp;&nbsp; 
    Contextual Inquiry, User Survey & Interview, Affinity Diagramming, Heuristic Evaluation
</li>
<li>-  &nbsp;&nbsp; 
    Empathy Map, Data Analysis, ExperimentDesign, A/B & Usability Testing, Mixpanel
</li>
<li>-  &nbsp;&nbsp; 
    Adobe Suite, Sketch, Invision, Adobe XD, Figma, Axure, Framer X, Balsamiq
</li>
<li>-  &nbsp;&nbsp; 
    Axure, Principle, Coreldraw, Unity, Adobe After Effect, Final Cut Pro HD, DVD Studio Pro
</li>
<li>-  &nbsp;&nbsp; 
    HTML, CSS, Javascript, React, Node.js, Ruby
</li> --}}
            </div>
        </div>
    </div>
</section>
@endsection
