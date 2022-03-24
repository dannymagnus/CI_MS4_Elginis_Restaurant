# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class About(models.Model):
    """
    A class for the about model
    """
    title = models.CharField(
        max_length=50
        )
    body = models.TextField(
        max_length=1000
        )
    image = models.ImageField(
        upload_to='about/'
        )

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        """
        Returns the about name string
        """
        return self.title


class Reason(models.Model):
    """
    A class for the reason model
    """
    title = models.CharField(
        max_length=50
        )
    body = models.TextField(
        max_length=500
        )

    class Meta:
        verbose_name = 'Reason'
        verbose_name_plural = 'Reasons'

    def __str__(self):
        """
        Returns the about name string
        """
        return self.title


class Chef(models.Model):
    """
    A class for the chef model
    """
    name = models.CharField(
        max_length=30
        )
    description = models.TextField(
        max_length=300
        )
    image = models.ImageField(
        upload_to='about/'
        )

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'

    def __str__(self):
        """
        Returns the chef name string
        """
        return self.name


class Comment(models.Model):
    """
    A class for the comment model
    """
    name = models.CharField(
        max_length=80
        )
    email = models.EmailField()
    body = models.TextField(500)
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    approved = models.BooleanField(
        default=False
        )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns comment body and name as a string
        """
        return f"Comment {self.body} by {self.name}"
