from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.

def contact_us(request):
    contact_form = ContactForm()
    contacted = False
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contacted = True
    context = {'contact_form': contact_form,
               'contacted': contacted,}
    
    return render(request,'contact/contact.html', context)