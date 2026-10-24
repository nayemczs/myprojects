from django.urls import path
from .views import login_user, logout_user, dashboard, vendor_register, customer_register, \
                   cart, add_to_cart, remove_from_cart, clear_cart, place_order, orders, mark_complete

app_name = 'users'
urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/<int:product_id>/add/', add_to_cart, name='cart_add'),
    path('cart/<int:product_id>/remove/', remove_from_cart, name='cart_remove'),
    path('cart/clear/', clear_cart, name='cart_clear'),
    path('cart/order/place/', place_order, name='place_order'),

    path('orders/', orders, name='orders'),
    path('orders/<int:product_id>/<int:item_id>/mark/', mark_complete, name='mark_order'),

    path('login/', login_user, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_user, name='logout'),
    path('register/', customer_register, name='customer_register'),
    path('register/vendor/', vendor_register, name='vendor_register'),
]
