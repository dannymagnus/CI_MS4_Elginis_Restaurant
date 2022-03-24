# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Carousel(models.Model):
    """
    A class for the carousel model
    """
    title = models.CharField(
        max_length=30
        )
    body = models.CharField(
        max_length=30,
        blank=True,
        default=''
        )
    image = models.ImageField(
        upload_to='home/'
        )

    def __str__(self):
        """
        Returns the carousel title
        """
        return self.title
