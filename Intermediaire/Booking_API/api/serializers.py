from rest_framework import serializers
from .models import Reservation, Room, Hotel
from django.contrib.auth.models import User

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = '__all__'
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
