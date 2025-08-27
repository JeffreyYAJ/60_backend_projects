from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=150)
    description= models.TextField()
    company= models.CharField(max_length=150)
    location= models.CharField(max_length=150)
    posted_on = models.DateTimeField(auto_now_add=True)