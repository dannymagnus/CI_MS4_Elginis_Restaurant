from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        
    def __str__(self):
        return self.title


class Reason(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Reason'
        verbose_name_plural = 'Reasons'
        
    def __str__(self):
        return self.title

    
    
class Chef(models.Model):
    name = models.CharField(max_length= 30)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='about/')
    
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'
        
    def __str__(self):
        return self.name
