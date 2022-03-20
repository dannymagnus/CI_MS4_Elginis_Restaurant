from django import forms
from .models import Reason, Contact
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        