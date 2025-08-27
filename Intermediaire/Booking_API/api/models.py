from django.db import models
from django.contrib.auth.models import User, AbstractUser


class AppUser(AbstractUser):
    name = models.CharField(max_length=150)
    role = models.CharField()

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out = models.DateField()
    
    # class Meta:
    #     unique_together = ( 'room', 'check_in_date', 'check_out')