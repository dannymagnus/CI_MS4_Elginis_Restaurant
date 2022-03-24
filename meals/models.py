# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.utils.text import slugify
from django.contrib import admin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Allergen(models.Model):
    """
    A class for the allergen model
    """
    name = models.CharField(
        max_length=50
        )
    image = models.ImageField(
        upload_to='allergens/',
        blank=True
        )

    def __str__(self):
        return self.name


class Meal(models.Model):
    """
    A class for the meal model
    """
    name = models.CharField(
        max_length=50
        )
    description = models.TextField(
        max_length=500
        )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        related_query_name='category'
        )
    lunch = models.BooleanField(
        default=False
        )
    dinner = models.BooleanField(
        default=False
        )
    calories = models.IntegerField(
        default=500
        )
    price = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        )
    vegetarian = models.BooleanField(
        default=False
        )
    vegan = models.BooleanField(
        default=False
        )
    allergens = models.ManyToManyField(
        Allergen, blank=True,
        related_name='allergens'
        )
    image = models.ImageField(
        upload_to='meals/',
        blank=True
        )
    slug = models.SlugField(
        blank=True,
        null=True
        )

    # Overide save function to create a slug on save -
    # courtesy of Mahmoud Ahmed
    def save(self, *args, **kwargs):
        """
        Function to take slug or create on if none exist
        """
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

    # Show object by name in admin panel
    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name


class Category(models.Model):
    """
    A class for the category model
    """
    name = models.CharField(
        max_length=50
        )

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name


class Drink(models.Model):
    """
    A class for the drink model
    """
    name = models.CharField(
        max_length=50
        )
    category = models.ForeignKey(
        'DrinkCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        related_query_name='category'
        )
    description = models.CharField(
        max_length=100,
        blank=True
        )

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name


class DrinkCategory(models.Model):
    """
    A class for the drinkcategory model
    """
    name = models.CharField(
        max_length=50
        )

    def __str__(self):
        """
        Returns the category name string
        Args:
            self (object): self.
        Returns:
            The category name string
        """
        return self.name
