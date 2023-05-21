from django.db import models

# Create your models here.

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
    material_status = models.CharField(max_length=50,choices=material)
    gender = models.CharField(max_length=50,choices=gen)
    phone = models.IntegerField()
    vcation_days = models.IntegerField()
    approved_vacation = models.IntegerField()
    salary = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return self.firstname + " " + self.lastname 
    