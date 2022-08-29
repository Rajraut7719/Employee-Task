from django.db import models

# Create your models here.

# Employee model
class Employee(models.Model):
    name=models.CharField(max_length=50)