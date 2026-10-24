from django.urls import path
from .views import index, about, contact, all_products, show_product, product_update, product_add, \
                   image_add, image_update, image_remove

app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('products/', all_products, name='all'),
    path('products/<int:product_id>/show/', show_product, name='show'),
    path('product/add/', product_add, name='add'),
    path('product/<int:product_id>/update/', product_update, name='update'),
    path('product/image/<int:product_id>/add/', image_add, name='image_add'),
    path('product/image/<int:product_id>/<int:image_id>/update/', image_update, name='image_update'),
    path('product/image/<int:product_id>/<int:image_id>/remove/', image_remove, name='image_remove')
]
