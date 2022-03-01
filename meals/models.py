from django.db import models

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=3, decimal_places=1)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    alergens = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals/')
    
    def __str__(self):
        return self.name