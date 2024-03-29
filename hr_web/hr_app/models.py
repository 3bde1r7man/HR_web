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
    phone = models.CharField(max_length= 100)
    vcation_days = models.IntegerField()
    approved_vacation = models.IntegerField()
    salary = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return self.firstname + " " + self.lastname 
    
class Vacation(models.Model):
    Status = [
        ('Submitted', 'Submitted'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=50)  
    fromDate = models.DateField()
    toDate = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=50,choices=Status) 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name


    