from django.shortcuts import render, redirect

# Create your views here.
#import the model so that all items can be retreived for the list
from .models import Meal, Category, Allergen, Drink, DrinkCategory

#view for all meal items
def meal_list(request):
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()
    
    context = {'meal_list':meal_list,
               'categories':categories,
               'allergens':allergens
               }
    
    return render(request, 'Meals/meal_list.html', context)


def lunch_menu(request):
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()
    
    context = {'meal_list':meal_list,
               'categories':categories,
               'allergens':allergens
               }
    
    return render(request, 'Meals/lunch_menu.html', context)

def dinner_menu(request):
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    allergens = Allergen.objects.all()
    
    context = {'meal_list':meal_list,
               'categories':categories,
               'allergens':allergens
               }
    
    return render(request, 'Meals/dinner_menu.html', context)

def drinks_menu(request):
    drinks = Drink.objects.all()
    categories = DrinkCategory.objects.all()
    
    context = {'drinks':drinks,
               'categories':categories,
               }
    
    return render(request, 'Meals/drinks_menu.html', context)


#takes the request and slug parameter from urls.py
def meal_information(request,slug):
    meal_information = Meal.objects.get(slug=slug)
    context = {'meal_information':meal_information}
    return render(request, 'Meals/meal_information.html', context)


def facebook(request):
    return redirect('http://www.facebook.com')