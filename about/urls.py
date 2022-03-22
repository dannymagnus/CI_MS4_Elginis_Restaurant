from django.urls import path
from . import views

#Provide an app name to fix namespace error
app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('delete/<comment_id>', views.delete_item, name = 'delete')
]