from django.db import models
from django.utils.text import slugify
from django.forms import CheckboxSelectMultiple
from django.contrib import admin


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class Allergen(models.Model):
    name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='allergens/', blank=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    #Acceptable categories = [starter, pasta, pizza, speciality, salad, dessert, drink]
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='category', related_query_name='category')
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    calories = models.IntegerField(default=500)
    price = models.DecimalField(max_digits=3, decimal_places=1)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    allergens = models.ManyToManyField(Allergen, blank=True, related_name='allergens')
    image = models.ImageField(upload_to='meals/', blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    #Overide save function to create a slug on save - courtesy of Mahmoud Ahmed
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

    #Show object by name in admin panel
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
