from django.shortcuts import render
from .models import Carousel

# Create your views here.

def home(request):
    carousel = Carousel.objects.all()
    context = {'carousel': carousel}
    
    return render(request,'home/index.html', context)