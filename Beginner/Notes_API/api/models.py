from django.db import models

class Student(models.Model):
    name = models.CharField(max_length= 150)
    
class Subject(models.Model):
    name = models.CharField(max_length= 50)

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()