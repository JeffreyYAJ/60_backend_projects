from django.db import models
import uuid

class Email(models.Model):
    email = models.EmailField(max_length=60, unique=True)
    is_verified= models.BooleanField(default= False)
    verification_token = models.UUIDField(editable= True, default=uuid.uuid4)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    