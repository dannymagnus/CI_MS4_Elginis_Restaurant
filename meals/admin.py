from django.contrib import admin

# Register your models here.

from .models import Meal, Category, Allergen, Drink, DrinkCategory


admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Allergen)
admin.site.register(Drink)
admin.site.register(DrinkCategory)



