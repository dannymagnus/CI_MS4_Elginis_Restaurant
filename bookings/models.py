# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Booking(models.Model):
    """
    A class for the booking model
    """
    name = models.CharField(
        max_length= 50
        )
    email = models.EmailField(
        max_length=70
        )
    phone = models.CharField(
        max_length=12
        )
    party_size = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        """
        Returns the booking name string
        """
        return self.name