from django import forms
from .models import Booking
from django.forms import ModelForm, TextInput, EmailInput, TimeInput
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'
    

class BookingForm(forms.ModelForm):
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
            'phone':TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'party_size':TextInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'date':DateInput(attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'time':TimeInput(attrs = {
                'class': "form-control timepicker",
                'min': "09:00",
                'max': "17:00",
                'style': 'max-width: 300px;',
                'step:':'600'
            })
            }
        
