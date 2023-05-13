from django import forms
from . import models

class AddEmployee1(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["emp_id","first_name", "last_name", "email",  "address"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'x',"placeholder":"First name","required": True,"id":"firstname"}),
            'last_name': forms.TextInput(attrs={'class': 'x1',"placeholder":"Last name","required": True,"id":"lastname"}),
            'email': forms.TextInput(attrs={'class': 'x2',"placeholder":"Your e-mail","required": True,"id":"email"}),
            'emp_id': forms.TextInput(attrs={'class': 'x3', 'placeholder': 'User id', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'x4',"placeholder":"Address","required": True,"id":"address"}),
            }
        
class AddEmployee2(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["matrial_status","gender","phone_number","salary"]

        widgets = {
            "matrial_status": forms.Select(attrs={"id": "materialStatus","required": True}, choices=models.Employee.MATRIAL_STATUS_CHOICES),
            "gender": forms.Select(attrs={"id": "gender","required": True,}, choices=models.Employee.GENDER_CHOICES),
            "phone_number": forms.TextInput(attrs={"id": "phoneNum","class": "x2","placeholder": "Phone number","required": True,}),
            "salary": forms.NumberInput(attrs={"id": "salary","class": "x6","placeholder": "Salary","required": True,}),
        }