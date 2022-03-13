from django.shortcuts import render
from .models import About, Chef, Reason

# Create your views here.

def about(request):
    about = About.objects.all()
    chefs = Chef.objects.all()
    reasons = Reason.objects.all()
    context = {
        'about': about,
        'chefs':chefs,
        'reasons': reasons
        }
    return render(request, 'about.html', context)