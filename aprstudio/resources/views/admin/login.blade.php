<!DOCTYPE html>
<html lang="en-us" dir="ltr">

<head>
    <title>Log in | AprStudio Admin Panel</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/base.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/nav_sidebar.css') }}">
    {{-- <script src="/static/admin/js/nav_sidebar.js" defer></script> --}}
    <link rel="stylesheet" type="text/css" href="{{ asset('css/login.css') }}">
    <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/responsive.css') }}">
    <meta name="robots" content="NONE,NOARCHIVE">
</head>

<body class=" login" data-admin-utc-offset="0">
    <!-- Container -->
    <div id="container">
        <!-- Header -->
        <div id="header">
            <div id="branding">
                <h1 id="site-name"><a href="/admin/">AprStudio Admin Area</a></h1>
            </div>
        </div>
        <!-- END Header -->
        <div class="main shifted" id="main">
            <div class="content">
                <!-- Content -->
                @include('includes._messages')
                <div id="content" class="colM">
                    <div id="content-main">
                        <form action="" method="post" id="login-form">
                            @csrf
                            <div class="form-row">
                                <label class="required" for="id_username">Email:</label>
                                <input type="email"
                                       name="email"
                                       class="@error('email') is-invalid @enderror"
                                       autofocus
                                       autocapitalize="none"
                                       autocomplete="email"
                                       maxlength="255"
                                       required
                                       value="{{ old('email') }}"
                                       id="id_username">
                                @error('email')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                            <div class="form-row">
                                <label class="required" for="id_password">Password:</label>
                                <input type="password"
                                       name="password"
                                       class="@error('password') is-invalid @enderror"
                                       autocomplete="current-password"
                                       required
                                       id="id_password">

                                @error('password')
                                    <ul class="errorlist"><li>{{ $message }}</li></ul>
                                @enderror
                            </div>
                            <div class="submit-row">
                                <input type="submit" value="Log in">
                            </div>
                        </form>

                    </div>
                    <br class="clear">
                </div>
                <!-- END Content -->
                <div id="footer"></div>
            </div>
        </div>
    </div>
    <!-- END Container -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"
            crossorigin="anonymous"></script>
</body>

</html>
