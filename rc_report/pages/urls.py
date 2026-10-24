from django.urls import path
from .views import index, free_report, profile, pro_report


app_name = 'pages'
urlpatterns = [
    path('', index, name='index'),
    path('free_report', free_report, name='free_report'),
    path('profile', profile, name='profile'),
    path('pro_report', pro_report, name='pro_report')
]
