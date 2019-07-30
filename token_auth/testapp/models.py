from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    rollno=models.IntegerField()
    subject=models.CharField(max_length=50)
