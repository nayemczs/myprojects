from django.urls import path
from .views import index, home, about_us, contact_us, account, products,wishlist,basket,terms,policy,delivery, show

app_name = 'pages'
urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('products/', products, name='products'),
    path('show/', show, name='show'),
    path('about_us/', about_us, name='about_us'),
    path('contact_us/', contact_us, name='contact_us'),
    path('account/', account, name='account'),
    path('wishlist/', wishlist, name='wishlist'),
    path('basket/', basket, name='basket'),
    path('terms/', terms, name='terms'),
    path('policy/', policy, name='policy'),
    path('delivery/', delivery, name='delivery'),

]
