# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports
# 3rd Party
from django.contrib import admin

# Internal
from .models import About, Reason, Chef, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Comment)
class ChefAdmin(Chef):
    """
    Admin class for chef
    """
    list_display = (
        'name',
        'bio',
        'image'
        )
    list_filter = (
        'name',
        )
    search_fields = (
        'name',
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin Clas for Comment Model
    """
    list_display = (
        'name',
        'body',
        'created_on',
        'approved',
        )
    list_filter = (
        'approved',
        'created_on',
        )
    search_fields = (
        'name',
        'email',
        'body',
        )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin Clas for Comment Model
    """
    list_display = (
        'title',
        'body',
        'image',
        )
    search_fields = (
        'title',
        'body',
        )


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    """
    Admin Class for Reason Model
    """
    list_display = (
        'title',
        'body',
        )
    search_fields = (
        'title',
        'body',
        )
