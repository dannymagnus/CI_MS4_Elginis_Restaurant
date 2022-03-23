# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin Class for Booking Model
    """
    list_display = (
        'name',
        'email',
        'phone',
        'party_size',
        'date',
        'time'
        )
    list_filter = (
        'name',
        'email',
        'date',
        'time')
    search_fields = (
        'name',
        'email',
        )
