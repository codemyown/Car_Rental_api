# rental/urls.py
from django.urls import path,include
from .views import book_car, booking_history
from rest_framework import routers
from .views import CarViewSet, BookingViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
   
    path('api/', include(router.urls)),
    path('book/<int:car_id>/', book_car, name='book_car'),
    path('booking_history/', booking_history, name='booking_history'),
    # Add more URLs as needed
]
