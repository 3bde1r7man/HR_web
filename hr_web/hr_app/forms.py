from django import forms
from . import models

class AddEmployee1(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["emp_id","first_name", "last_name", "email",  "address"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'x',"placeholder":"First name","id":"firstname"}),
            'last_name': forms.TextInput(attrs={'class': 'x1',"placeholder":"Last name","id":"lastname"}),
            'email': forms.TextInput(attrs={'class': 'x2',"placeholder":"Your e-mail","id":"email"}),
            'emp_id': forms.TextInput(attrs={'class': 'x3', 'placeholder': 'User id'}),
            'address': forms.TextInput(attrs={'class': 'x4',"placeholder":"Address","id":"address"}),
            }
        
class AddEmployee2(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["matrial_status","gender","phone_number","salary","date_of_birth","vacation_number","approved_vacation_number"]
        widgets = {
            "matrial_status": forms.Select( choices=models.Employee.MATRIAL_STATUS_CHOICES),
            "gender": forms.Select(choices=models.Employee.GENDER_CHOICES),
            "phone_number": forms.TextInput(attrs={"class": "x2","placeholder": "Phone number"}),
            "salary": forms.NumberInput(attrs={"class": "x6","placeholder": "Salary"}),
            "date_of_birth": forms.DateInput(attrs={"class": "x6","placeholder": "Date of birth","type":"date"}),
            "vacation_number": forms.NumberInput(attrs={"class": "x6","placeholder": "Vacation number"}),
        }
class EditEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"
        widgets = {
            "emp_id":forms.HiddenInput(),
            "date_of_birth": forms.DateInput(attrs={"placeholder": "Date of birth","type":"date"}),
        }
