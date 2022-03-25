# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render

# Internal:
from .models import Carousel
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home(request):
    """
    A view to home page with rotating carousel
    Args:
        request (object): HTTP request object.
    Returns:
        Render of home page with context
    """
    carousel = Carousel.objects.all()
    context = {'carousel': carousel}

    return render(request, 'home/index.html', context)
