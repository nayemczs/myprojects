@if (session('success'))
    @include('includes._alert', ['tag' => 'success', 'message' => session('success')])
@endif

@if (session('info'))
    @include('includes._alert', ['tag' => 'info', 'message' => session('error')])
@endif

@if (session('warning'))
    @include('includes._alert', ['tag' => 'warning', 'message' => session('success')])
@endif

@if (session('error'))
    @include('includes._alert', ['tag' => 'danger', 'message' => session('error')])
@endif

