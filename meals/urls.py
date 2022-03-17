from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'meals'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('lunch_menu', views.lunch_menu, name='lunch_menu'),
    path('dinner_menu', views.dinner_menu, name='dinner_menu'),
    path('drinks_menu', views.drinks_menu, name='drinks_menu'),
    path('<slug>:slug', views.meal_information, name='meal_information'),
    path('facebook', views.facebook, name='facebook'),
]