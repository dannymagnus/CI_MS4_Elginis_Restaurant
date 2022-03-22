from django.shortcuts import render
from .models import Booking
from .forms import BookingForm
# Create your views here.

def make_booking(request):
    """
    A view to display a booking form, and retrieve user entries
    Args:
        request (object): HTTP request object.
    Returns:
        Render of booking page and form page with context
    """
    booking_form = BookingForm()
    booked = False
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            booked = True
    context = {'form': booking_form,
               'booked': booked,}
    
    return render(request,'bookings/bookings.html', context)