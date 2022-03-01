from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'meals'

urlpatterns = [
    path('', views.meal_list ),
]