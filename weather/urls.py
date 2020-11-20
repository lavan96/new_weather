from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('current', views.current_loc, name='current_location'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]