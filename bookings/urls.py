from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'bookings'

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
]