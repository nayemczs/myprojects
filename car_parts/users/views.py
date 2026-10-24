from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import RegistrationForm, VendorRegistrationForm, LoginForm
from products.models import Product
from products.forms import ProductForm
from p_shope.decorators import anonymous_user, buyer_required, vendor_required


# Create your views here.
@anonymous_user
def vendor_register(request):
    registration_form = VendorRegistrationForm(request.POST or None, request.FILES or None)
    if registration_form.is_valid():
        user = registration_form.save(commit=False)
        data = registration_form.cleaned_data
        user.username = user.email
        user.set_password(user.password)
        user.is_vendor = True
        user.save()
        user.create_vendor_profile(
            name=data['name'],
            region=data['region'],
            country=data['country'],
            city=data['city'],
            address=data['address'],
            image=data['image']
        )
        messages.success(request, _('Account has been registered SUCCESSFULLY'))
        return redirect('users:login')
    return render(request, 'vendor_register.html', {'registration_form': registration_form})


@anonymous_user
def customer_register(request):
    registration_form = RegistrationForm(request.POST or None, request.FILES or None)
    if registration_form.is_valid():
        user = registration_form.save(commit=False)
        data = registration_form.cleaned_data
        user.username = user.email
        user.set_password(user.password)
        user.save()
        user.create_user_profile(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            image=data['image']
        )
        messages.success(request, _('Account has been registered SUCCESSFULLY'))
        return redirect('users:login')
    return render(request, 'customer_register.html', {'registration_form': registration_form})


@login_required(login_url='users:login')
def dashboard(request):
    if request.user.is_vendor:
        vendor = request.user.vendor_profile
        products = vendor.products.all()
        context = {
            'product_form': ProductForm(),
            'products': products
        }
        return render(request, 'vendor_dashboard.html', context)
    else:
        context = request.user.profile.order_info()
        return render(request, 'dashboard.html', context)


@anonymous_user
def login_user(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        data = login_form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, _("You're logged in Successfully"))
                return redirect('users:dashboard')
        messages.error(request, _('Email or Password does not match'))
    return render(request, 'login.html', {'login_form': login_form})


@login_required(login_url='users:login')
def logout_user(request):
    if not request.user.is_vendor:
        request.user.profile.remove_cart()
    logout(request)
    messages.success(request, _("You're logged out Successfully"))
    return redirect('products:index')


@login_required(login_url='users:login')
@buyer_required
def cart(request):
    user_profile = request.user.profile
    user_cart = user_profile.get_cart(request.session.session_key)
    cart_items = user_cart.cart_items.all()
    cart_total = user_cart.total

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    return render(request, 'cart.html', context)


@login_required(login_url='users:login')
@buyer_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST['quantity'])
    request.user.profile.add_to_cart(request.session.session_key, product, quantity)
    return redirect('users:cart')


@login_required(login_url='users:login')
@buyer_required
def remove_from_cart(request, product_id):
    request.user.profile.remove_from_cart(request.session.session_key, product_id)
    return redirect('users:cart')


@login_required(login_url='users:login')
@buyer_required
def clear_cart(request):
    request.user.profile.clear_cart(request.session.session_key)
    return redirect('users:cart')


@login_required(login_url='users:login')
@buyer_required
def place_order(request):
    request.user.profile.place_order(request.session.session_key)
    messages.success(request, _('Your order has been placed Successfully'))
    return redirect('users:cart')


@login_required(login_url='users:login')
@vendor_required
def orders(request):
    context = request.user.vendor_profile.order_info()
    return render(request, 'orders_vendor.html', context)


@login_required(login_url='users:login')
@vendor_required
def mark_complete(request, product_id, item_id):
    request.user.vendor_profile.mark_order(product_id, item_id)
    messages.success(request, _('Order Marked'))
    return redirect('users:orders')
