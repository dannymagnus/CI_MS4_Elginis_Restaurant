from django.db import models
from django.utils.text import slugify

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=3, decimal_places=1)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    alergens = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)
    
    #Overide save function to create a slug on save - courtesy of Mahmoud Ahmed
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    #Show object by name in admin panel
    def __str__(self):
        return self.name