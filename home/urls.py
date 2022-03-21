from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]