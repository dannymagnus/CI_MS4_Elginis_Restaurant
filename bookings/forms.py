from django import forms
from .models import Booking

class BookTableForm(models.ModelForm):
    class Meta:
        name = Booking
        fields = '__all__'
