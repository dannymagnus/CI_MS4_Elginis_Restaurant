# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Contact, Reason
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin Class for Contact Model
    """
    list_display = (
        'name',
        'reason',
        'message',
        'phone',
        'email'
        )
    list_filter = (
        'name',
        'reason',
        'email'
        )
    search_fields = (
        'name',
        'email',
        )


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    """
    Admin Class for Reason Model
    """
    list_display = (
        'reason',
        )
    search_fields = (
        'reason',
        )