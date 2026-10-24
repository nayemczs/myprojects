from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

# Create your views here.
def single_product(request):
    return render(request, 'pages/single_product.html')
