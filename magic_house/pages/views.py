from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def account(request):
    return render(request, 'account.html')


def products(request):
    return render(request, 'product_listing.html')


def show(request):
    return render(request, 'single_product_listing.html')

def contactus(request):
    return render(request, 'contactus.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def basket(request):
    return render(request, 'basket.html')

def terms(request):
    return render(request, 'terms.html')

def policy(request):
    return render(request, 'policy.html')

def delivery(request):
    return render(request, 'delivery.html')
