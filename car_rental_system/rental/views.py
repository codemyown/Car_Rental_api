# rental/views.py
from django.shortcuts import render, redirect
from .models import Car, Booking
from django.contrib.auth.decorators import login_required
from .serializers import CarSerializer, BookingSerializer
from rest_framework import viewsets



def book_car(request, car_id):
    # Handle car booking logic
    return redirect('booking_history')

def booking_history(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'booking_history.html', {'bookings': bookings})

# Add more views as needed

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
