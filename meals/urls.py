from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'meals'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug>:slug', views.meal_information, name='meal_information'),
    path('facebook', views.facebook, name='facebook'),
]