from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    saddr=models.CharField(max_length=100)
    sschool=models.CharField(max_length=50)

class StudentSignup(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=30)
    saddr=models.CharField(max_length=100)
    smobilenumber=models.IntegerField()
    semail=models.EmailField()
