from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
    	return self.name
    
class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
    	return self.customer
 
