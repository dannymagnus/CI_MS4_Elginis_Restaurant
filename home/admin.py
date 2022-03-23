# Imports
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party
from django.contrib import admin

# Internal
from .models import Carousel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """
    Admin Class for Carousel Model
    """
    list_display = (
        'title',
        'body',
        'image',
        )
    list_filter = (
        'title',
        )
    search_fields = (
        'title',
        'body',
        )