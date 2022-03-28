# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, TimeInput

# Internal
from .models import Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):
    """
    A class for date input picker
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    A class for date input picker
    """
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """
    A class for booking form
    """
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'party_size': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'time': TimeInput(attrs={
                'class': "form-control timepicker",
                'min': "12:00",
                'max': "21:00",
                'style': 'max-width: 300px;',
                'step': '900'
            })
            }
