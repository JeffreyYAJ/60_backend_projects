from django.db import models
from django.core.validators import  MinLengthValidator, MaxLengthValidator

class Feedback(models.Model):
    username = models.CharField(max_length=50)
    stars = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    comment = models.TextField()
    
    