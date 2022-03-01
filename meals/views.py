from django.shortcuts import render

# Create your views here.
#import the model so that all items can be retreived for the list
from .models import Meal

#view for all meal items
def meal_list(request):
    meal_list = Meal.objects.all()
    
    context = {'meal_list':meal_list}
    
    return render(request, 'Meals/meal_list.html', context)



#takes the request and slug parameter from urls.py
def meal_information(request,slug):
    pass