# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, get_object_or_404

# Internal:
from .models import Meal, Category, Allergen, Drink, DrinkCategory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def meal_list(request):
    """
    A view to show all products
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()

    context = {'meal_list': meal_list,
               'categories': categories,
               'allergens': allergens
               }

    return render(request, 'Meals/meal_list.html', context)


def lunch_menu(request):
    """
    A view to show all lunch products, filtered by boolean field
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()

    context = {'meal_list': meal_list,
               'categories': categories,
               'allergens': allergens
               }

    return render(request, 'Meals/lunch_menu.html', context)


def dinner_menu(request):
    """
    A view to show all dinner products, filtered by boolean field
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()

    context = {'meal_list': meal_list,
               'categories': categories,
               'allergens': allergens
               }

    return render(request, 'Meals/dinner_menu.html', context)


def drinks_menu(request):
    """
    A view to show all drink products
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    drinks = Drink.objects.all()
    categories = DrinkCategory.objects.all()

    context = {'drinks': drinks,
               'categories': categories,
               }

    return render(request, 'Meals/drinks_menu.html', context)


# takes the request and slug parameter from urls.py
def meal_information(request, slug):
    """
    A view to detailed meal view, all meal information
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    meal_information = get_object_or_404(Meal, slug=slug)
    context = {'meal_information': meal_information}
    return render(request, 'Meals/meal_information.html', context)
