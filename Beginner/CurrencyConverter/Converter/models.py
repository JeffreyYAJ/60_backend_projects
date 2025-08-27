from django.db import models

class Conversions(models.Model):
    value = models.FloatField()
    converted = models.FloatField()
    #time = models.DateField(auto_now_add=True)