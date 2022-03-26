# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports
# 3rd Party
from django.urls import path

# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('delete/<comment_id>', views.delete_item, name='delete'),
    path('edit/<comment_id>', views.edit_item, name='edit')
]
