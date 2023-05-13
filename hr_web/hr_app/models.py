from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions  import ValidationError
import re
from datetime import date

class Employee(models.Model):
    MATRIAL_STATUS_CHOICES = (
        ("Single", "Single"),
        ("Married", "Married"),
        ("Widowed","Widowed"),
        ("Divorced", "Divorced"),
        ("Separated","Separated"),
    )
    GENDER_CHOICES = (
        ("Male","Male"),
        ("Female","Female")
    )
    emp_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    matrial_status = models.CharField(choices=MATRIAL_STATUS_CHOICES,max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=30)
    phone_number = models.CharField(max_length=15)
    salary = models.IntegerField(validators=[MinValueValidator(2000,message="Value must be greater than or equal to 2000."),
                                             MaxValueValidator(6000,message="Value must be less than or equal to 6000.")])
    date_of_birth = models.DateField()
    vacation_number = models.IntegerField(validators=[  MinValueValidator(1,message="Value must be greater than or equal to 1."),
                                                        MaxValueValidator(10,message="Value must be less than or equal to 10.")])
    aprroved_vacation_number = models.IntegerField(validators=[ MinValueValidator(1,message="Value must be greater than or equal to 1."),
                                                                MaxValueValidator(10,message="Value must be less than or equal to 10.")])
    
    def clean(self):
        pattern = r'^(\+2)?01(0|1|2)\d{8}$'
        if not re.match(pattern, self.phone_number):
            raise ValidationError(
                f'{self.phone_number} is not a valid phone number',
                params={'value': self.phone_number},
            )
        if self.date_of_birth.year < date.today().year- 21:
            raise ValidationError(
                f'Employee must be older than 21 years old',
            )

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
