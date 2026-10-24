from django.urls import path
from .views import index, watches


app_name = 'pages'
urlpatterns = [
    path('', index, name='index'),
    path('watches/', watches, name='watches')
]
