from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    party_size = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.name