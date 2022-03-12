from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
# Create your views here.

def make_booking(request):
    booking_form = BookingForm()
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
    context = {'form': booking_form}
    
    return render(request,'bookings/bookings.html', context)