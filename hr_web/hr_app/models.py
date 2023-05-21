from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions  import ValidationError
import re
from datetime import date

class Employee(models.Model):
    material = [
        ('single','single'),
        ('married','married'),
        ('widowed','widowed'),
        ('divorced','divorced'),
        ('separated','separated'),
    ]
    gen = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    userid = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    material_status = models.CharField(max_length=50,choices=material, null=True)
    gender = models.CharField(max_length=50,choices=gen)
    phone = models.CharField(max_length= 20, null=True)
    vcation_days = models.IntegerField(null=True)
    approved_vacation = models.IntegerField(null=True)
    salary = models.IntegerField()
    date = models.DateField(null = True)

class Vacation(models.Model):
    STATUS_CHOICES = (
        ("Submitted", "Submitted"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected")
    )
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    Reason = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_Name = models.CharField(max_length=50, null=True)
