from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def free_report(request):
    return render(request, 'pages/free_report.html')


def profile(request):
    return render(request, 'pages/profile.html')


def pro_report(request):
    return render(request, 'pages/pro_report.html')
