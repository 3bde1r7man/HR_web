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
        exclude = ['emp_id']
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"placeholder": "Date of birth","type":"date"}),
        }

class vacationForm(forms.ModelForm):
    class Meta:
        model = models.Vacation
        fields = ["employee","emp_Name","from_date","to_date", "Reason"]
        widgets = {
            "employee": forms.TextInput(attrs={"id": "emp-ID","class": "eid","placeholder": "ID", "disabled": "True",}),
            "emp_Name": forms.TextInput(attrs={"id": "emp-Name","class": "en","placeholder": "Name", "disabled": "True",}),
            "from_date": forms.DateInput(attrs={"id": "from-Date", "class": "fD", "required": "True", "min": "2023-04-17", "max": "2023-12-12"}),
            "to_date": forms.DateInput(attrs={"id": "to-Date", "class": "tD", "required": "True", "min": "2023-04-17", "max": "2023-12-12"}),    
            "Reason": forms.Textarea(attrs={"id": "Reason","class": "rs","placeholder": "Enter The Reason","cols": "30", "rows": "5", "required": "True",}),
        }
    

