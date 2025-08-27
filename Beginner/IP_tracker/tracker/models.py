from django.db import models
 
class Victim(models.Model):
    ip_address = models.GenericIPAddressField()
    city = models.CharField(max_length=70, null = True)
    region = models.CharField(max_length= 40, null = True)
    country = models.CharField(max_length=80, null = True)
    longitude = models.FloatField(null= True)
    latitude = models.FloatField(null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    