from django.urls import path
from .views import index, single_product


app_name = 'pages'
urlpatterns = [
    path('', index, name='index'),
    path('single_product', single_product, name='single_product')
]
