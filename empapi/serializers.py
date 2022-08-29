from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name']