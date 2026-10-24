from django.urls import path
from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('<str:place_id>/explore/', views.explore, name='explore'),
    path('<str:place_id>/explore/landscapes/<str:landscape>/', views.explore, name='explore_landscapes'),
    path('<str:place_id>/explore/interests/<str:interest>/', views.explore, name='explore_interests'),
    path(
        '<str:place_id>/explore/<str:destination_id>/',
        views.explore_region_or_destination,
        name='explore_destination'
    ),
    path('<str:place_id>/regions/', views.regions, name='regions'),
    path('<str:place_id>/regions/lands/<str:filter_key>/', views.regions, name='explore_lands'),
    path('<str:place_id>/regions/<str:region_id>/', views.explore_region_or_destination, name='explore_region'),
    path('hotels/', views.hotel_list, name='hotels'),
    path('hotels/<str:hotel_id>/', views.hotel_show, name='hotel_show'),
    path('houses/rents/', views.house_rent_listing, name='house_rents'),
    path('houses/rents/<str:house_id>/', views.house_rent_single_page, name='house_rent_show'),
    path('houses/sales/', views.house_sale_listing, name='house_sales'),
    path('houses/sales/<str:house_id>/', views.house_sale_single, name='house_sale_show')
]
