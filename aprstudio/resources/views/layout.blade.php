<!doctype html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link href='https://fonts.googleapis.com/css?family=Roboto:400,700,500' rel='stylesheet' type='text/css'>
    <!-- Body font -->
    <link href='https://fonts.googleapis.com/css?family=Lato:300,400' rel='stylesheet' type='text/css'>
    <!-- Navbar font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Azeret+Mono&family=Kaisei+Tokumin&display=swap"
          rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Abhaya+Libre&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://kit.fontawesome.com/11988d7f79.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="{{ asset('css/reset.css') }}">
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
    <link rel="stylesheet" href="{{ asset('css/mobile.css') }}">

    @section('styles')
    @show

    <title>APR Studio</title>
</head>

<body>
<div class="body">
    <main class="background_body">

        <section class="container-fluid pt-4 custom_menu_div" id="menu_div" style="">
            <div class="header_cross">
                <p class="right_sidebar right_top" id="cross"><img src="/img/Menu.png"
                                                                   style="width: 55px; height: 31px;"
                                                                   alt=""></p>
            </div>
            <div class="row  p-0 nav_links">
                <div class="col-md-12  p-0">
                    <div class="container p-2 pt-4">
                        <ul class="text-center" id="">
                            <li class="custom_nav_manu">
                                <a href="{{ route('index') }}"><h2>HOME</h2></a>
                            </li>
                            <li class="custom_nav_manu">
                                <a href="{{ route('index') }}"><h2>PROJECTS</h2></a>

                            </li>
                            <li class="custom_nav_manu">
                                <a href="{{ route('about') }}"><h2>ABOUT</h2></a>

                            </li>
                            <li id="contact_menu" class="custom_nav_manu">
                                <a href=""><h2>CONTACT</h2></a>
                            </li>

                        </ul>
                    </div>
                </div>
            </div>
            <div class="container contact_div py-4 pe-5" style="    padding-left: 100px;    background-color: #262626;">
                <div class="row">
                    <div class="col-lg-8 col-12">
                        <p class="text-white custom_contact_header">A simple hello could lead
                            to a million things</p>
                        <div>
                            <p class="fw-bold text-white custom_contact_location">Contact</p>
                            <div style="margin-left: 10px">
                                <p class="custom_contact_text">Get in Touch With Us: <span class="text-white">info@apr.com</span>
                                </p>
                                <p class="custom_contact_text">Work With Us: <span
                                        class="text-white">business@apr.com</span></p>
                                <div class="d-flex justify-content-between mt-3">
                                    <p class="text-white">We’re working and looking to add value to your project!</p>
                                    <hr>
                                </div>
                            </div>
                            <hr style="margin-top: 15px">


                        </div>
                    </div>
                    <div class="col-lg-4 col-12">
                        <div class="container-contact100">
                            <div class="wrap-contact100">
                                <form class="contact100-form validate-form">
                                    <div class="wrap-input100 validate-input" data-validate="Name is required">
                                        <input class="input100" id="name" type="text" name="name" placeholder="Name">
                                        <label class="label-input100" for="phone">
                                                <span>
                                                    <i class="fas fa-user" style="color: black;"></i>
                                                </span>
                                        </label>
                                    </div>

                                    <div class="wrap-input100 validate-input"
                                         data-validate="Valid email is required: ex@abc.xyz">
                                        <input class="input100" id="email" type="text" name="email" placeholder="Email">
                                        <label class="label-input100" for="phone">
                                                <span>
                                                    <i class="fas fa-envelope" style="color: black;"></i>
                                                </span>
                                        </label>
                                    </div>

                                    <div class="wrap-input100 validate-input" data-validate="Comment is required">
                                        <textarea class="input100" name="message" placeholder="Comment"></textarea>
                                        <label class="label-input100" for="phone">
                                                <span>
                                                    <i class="fas fa-pencil-alt" style="color: black;">
                                                    </i></span>
                                        </label>
                                    </div>
                                    <div class="mt-4">
                                        <button class="btn custom_contact_btn">Send</button>
                                    </div>
                                    <div style="margin-left: 15px;  margin-top: 65px; ">
                                        <p class="text-white custom_contact_location">
                                            <span class="text-white" style="font-size: 24px">Brooklyn, NY</span>
                                            <span>
                                                <img class="mb-1" width="28" src="img/location.svg" alt=""></span></p>

                                        <hr style="    margin: 41px auto;
                                            margin-bottom: 0px;">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <header class="container text-right py-5" id="main_header">
            <p class="right_sidebar right_top" id="header_icon"><img id="head_icon" src="/img/vector.svg"
                                                                     style="width: 55px; height: 31px;" alt=""></p>
        </header>
        <div class="left_sidebar left_top">
            <a href="{{ route('index') }}"><img id="first_one" src="/img/first_one.png" width="28" alt=""></a>
        </div>
        <div class="left_sidebar left_bottom">
            <img id="plus_one" src="/img/plus.png" width="33" alt="">
        </div>
        <div class="right_sidebar right_bottom" class="right_sidebar text-end">
            <div>
                <p>Follow <span><a style="margin-top:5px" class="custom_social"
                                   href="#" id="fb">&nbsp;FB</a>&nbsp;-&nbsp;
                                   <a class="custom_social" id="ins" href="#">INS &nbsp;</a> -&nbsp;
                                   <a class="custom_social" href="#" id="lin">LIN</a></span></p>
            </div>
        </div>
        @include('includes._navbar')
        @include('includes._messages')

        @yield('body')
        {{-- <a href="#" class="scrolltotop"><i class="fa fa-arrow-up"></i></a> <!-- Scroll to top button --> --}}
    </main>


</div><!-- body ends -->
<script>
    const menuIcon = document.getElementById('header_icon')
    const contactMenuIcon = document.getElementById('head_icon')
    const rightBottom = document.querySelector('.right_bottom')
    const contactMenu = document.getElementById('contact_menu')
    const menuCross = document.getElementById('cross')
    const plus = document.getElementById('plus_one')
    const firstOne = document.getElementById('first_one')
    const menuDiv = document.getElementById('menu_div')
    const customSocial = document.getElementsByClassName('custom_social')
    const fb = document.getElementById('fb')
    const ins = document.getElementById('ins')
    const lin = document.getElementById('lin')
    let contactButtonClicked = false

    function show_menu_white() {
        rightBottom.style.color = 'white'
        fb.style.color = 'white'
        ins.style.color = 'white'
        lin.style.color = 'white'
        plus.setAttribute('src', '/img/Plus_white.png')
        firstOne.setAttribute('src', '/img/untilt.png')
    }

    function hide_menu_white() {
        rightBottom.style.color = 'black'
        fb.style.color = 'black'
        ins.style.color = 'black'
        lin.style.color = 'black'
        plus.setAttribute('src', '/img/plus.png')
        firstOne.setAttribute('src', '/img/first_one.png')
    }

    menuIcon.addEventListener('click', () => {
        menuDiv.classList.add('menu_active')
        show_menu_white();
    })

    menuCross.addEventListener('click', hide_menu)

    menuDiv.addEventListener('click', (event) => {
        if (event.target.id === 'menu_div')
            hide_menu()
    })

    function hide_menu() {
        menuDiv.classList.remove('menu_active', 'contact_active')
        hide_menu_white()
        contactButtonClicked = false
    }

    plus.addEventListener('click',showContact)
    contactMenu.addEventListener('click', showContact)
    function showContact(event) {
        event.preventDefault()
        menuDiv.classList.toggle('contact_active')
        if (!contactButtonClicked) {
            show_menu_white()
            contactButtonClicked = true
        } else if (!menuDiv.classList.contains('menu_active')) {
            hide_menu_white()
            contactButtonClicked = false
    }
    }
</script>
<script src="{{ asset('scripts/jquery-1.11.1.min.js') }}"></script>
<script src="{{ asset('scripts/bootstrap.min.js') }}"></script>
<script src="{{ asset('scripts/isotope.pkgd.min.js') }}"></script>
<script src="{{ asset('scripts/theme.js') }}"></script>

@section('scripts')
@show
</body>
</html>
