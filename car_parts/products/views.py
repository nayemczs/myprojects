from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.utils.translation import gettext as _
from .forms import ProductForm, ProductUpdateForm, SearchForm, ImageForm
from .models import Product
from p_shope.decorators import buyer_required, vendor_required


# Create your views here.
def index(request):
    models = Product.objects.values_list('model_name', flat=True).distinct()
    parts = Product.objects.values_list('part_name', flat=True).distinct()
    regions = Product.objects.values_list('vendor__region', flat=True).distinct()
    countries = Product.objects.values_list('vendor__country', flat=True).distinct()
    cities = Product.objects.values_list('vendor__city', flat=True).distinct()
    context = {
        'models': models,
        'parts': parts,
        'regions': regions,
        'countries': countries,
        'cities': cities
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def all_products(request):
    search_form = SearchForm(request.POST)
    if search_form.is_valid():
        data = request.POST
        products = Product.apply_filters(data.getlist('part_name'), data.getlist('model_name'), data['area'])
        return render(request, 'shop.html', {'products': products})
    messages.error(request, _("Please make sure you've selected a Model a Part and an Area"))
    return redirect('products:index')


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()
    return render(request, 'shop-details.html', {'product': product, 'images': images})


@login_required(login_url='users:login')
@vendor_required
def product_add(request):
    if request.method == 'GET':
        return redirect('users:dashboard')

    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid():
        new_product = product_form.save(commit=False)
        request.user.vendor_profile.add_product(new_product, request.FILES.getlist('images'))
        messages.success(request, _('Product Added'))
        return redirect('users:dashboard')
    return render(request, 'vendor_dashboard.html', {'product_form': product_form})


@login_required(login_url='users:login')
@vendor_required
def product_update(request, product_id):
    try:
        product = request.user.vendor_profile.products.get(id=product_id)
    except ObjectDoesNotExist:
        raise PermissionDenied(_('Product does NOT exist'))

    data = {
        'model_name': product.model_name,
        'part_name': product.part_name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity
    }
    product_update_form = ProductUpdateForm(request.POST or None, initial=data)

    if product_update_form.is_valid():
        updated_product = product_update_form.save(commit=False)
        request.user.vendor_profile.update_product(product, updated_product)
        messages.success(request, _('Product Updated'))

    context = {
        'product_update_form': product_update_form,
        'product_id': product_id,
        'images': product.images.all()
    }
    return render(request, 'product_edit.html', context)


@login_required(login_url='users:login')
@vendor_required
def image_add(request, product_id):
    if request.method == 'GET':
        return redirect('users:dashboard')

    image_form = ImageForm(request.POST, request.FILES or None)
    if image_form.is_valid():
        request.user.vendor_profile.add_product_image(product_id, image_form.cleaned_data['image'])
        messages.success(request, _('Image Added'))
    return redirect('products:update', product_id)


@login_required(login_url='users:login')
@vendor_required
def image_update(request, product_id, image_id):
    if request.method == 'GET':
        return redirect('users:dashboard')

    image_form = ImageForm(request.POST, request.FILES or None)
    if image_form.is_valid():
        request.user.vendor_profile.update_product_image(product_id, image_id, image_form.cleaned_data['image'])
        messages.success(request, _('Image Updated'))
    print(image_form.errors)
    return redirect('products:update', product_id)


@login_required(login_url='users:login')
@vendor_required
def image_remove(request, product_id, image_id):
    request.user.vendor_profile.remove_product_image(product_id, image_id)
    messages.success(request, _('Image Removed'))
    return redirect('products:update', product_id)
