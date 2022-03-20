from django.db import models

# Create your models here.
class Contact(models.Model):
    reason = models.ForeignKey('Reason', on_delete=models.CASCADE, related_name='reasons')
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    postcode = models.CharField(max_length= 10)
    street_address = models.CharField(max_length=100)
    message = models.TextField(max_length = 300)
        
    def __str__(self):
        return self.name
    
    
class Reason(models.Model):
    reason = models.CharField(max_length=100)
    
    def __str__(self):
        return self.reason