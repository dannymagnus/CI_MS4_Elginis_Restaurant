from django.db import models

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=30, blank=True, default='')
    image = models.ImageField(upload_to='home/')
    
    def __str__(self):
        return self.title