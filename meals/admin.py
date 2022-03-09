from django.contrib import admin

# Register your models here.

from .models import Meal, Category, Allergen


admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Allergen)


