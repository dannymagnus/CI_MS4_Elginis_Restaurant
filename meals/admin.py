# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Meal, Category, Allergen, Drink, DrinkCategory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    """
    Admin Class for Meal Model
    """
    list_display = (
        'name',
        'description',
        'category',
        'lunch',
        'dinner',
        'calories',
        'price',
        'vegetarian',
        'vegan',
        'image',
        )
    list_filter = (
        'category',
        'lunch',
        'dinner',
        'vegetarian',
        'vegan',
        'allergens')
    search_fields = (
        'name',
        'allergens',
        'price',
        'vegetarian',
        'vegan',
        'lunch',
        'dinner',
        'category',
        )


@admin.register(Category)
class MealAdmin(admin.ModelAdmin):
    """
    Admin Class for Category Model
    """
    list_display = (
        'name',
    )


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    """
    Admin Class for Allergen Model
    """
    list_display = (
        'name',
    )


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    """
    Admin Class for Drink Model
    """
    list_display = (
        'name',
        'category',
        'description',
        )
    list_filter = (
        'category',
        )
    search_fields = (
        'name',
        'description',
        'category',
        )


@admin.register(DrinkCategory)
class AllergenAdmin(admin.ModelAdmin):
    """
    Admin Class for DrinkCategory Model
    """
    list_display = (
        'name',
    )
