<!DOCTYPE html>
<html lang="en-us" dir="ltr">
<head>
    <title> AprStudio Admin Area</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/base.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/nav_sidebar.css') }}">
    {{-- <script src="/static/admin/js/nav_sidebar.js" defer></script> --}}
    <link rel="stylesheet" type="text/css" href="{{ asset('css/forms.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/list.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/dashboard.css') }}">
    <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/responsive.css') }}">
    <meta name="robots" content="NONE,NOARCHIVE">
    @section('styles')
    @show

</head>

<body class=" app-pages model-watch change-form" data-admin-utc-offset="0">

    <!-- Container -->
    <div id="container">
        <!-- Header -->
        <div id="header">
            <div id="branding">
                <h1 id="site-name"><a href="/admin/">AprStudio Admin Area</a></h1>
            </div>
            <div id="user-tools"> Welcome, <strong>AprStudio_admin</strong>. <a href="/" target="_blank">View site</a> /
{{--                <a href="/admin/password_change/">Change password</a> /--}}
                <a href="{{ route('logout') }}">Log out</a>
            </div>
        </div>
        {{-- <!-- END Header -->
        <div class="breadcrumbs">
            <a href="/admin/">Home</a>
            &rsaquo; <a href="/admin/pages/">Pages</a>
            &rsaquo; <a href="/admin/pages/watch/">Protfolio</a>
            &rsaquo; Add Protfolio
        </div> --}}
        @section('body')
            <div class="main shifted" id="main">
                @include('admin.includes._sidebar')
                <div class="content">
                    @include('includes._messages')
                    @yield('content')
                </div>
            </div>
        @show
    </div>
    <!-- END Container -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"
            crossorigin="anonymous"></script>
    @section('scripts')
    @show
</body>

</html>
