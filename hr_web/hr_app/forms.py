from django import forms
from . import models


class AddEmployee1(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["firstname", "lastname", "email", "userid", "address"]
        widgets = {
            "firstname": forms.TextInput(attrs={"class": "x", "placeholder": "First name", "required": True, "id": "firstname"}),
            "lastname": forms.TextInput(attrs={"class": "x1", "placeholder": "Last name", "required": True, "id": "lastname"}),
            "email": forms.EmailInput(attrs={"class": "x2", "placeholder": "Your email address", "required": True, "id": "email"}),
            "userid": forms.NumberInput(attrs={"class": "x3", "placeholder": "User id", "required": True, "min": "1", "max": "2000", "id": "userid"}),
            "address": forms.TextInput(attrs={"class": "x4", "placeholder": "address", "required": True, "id": "address", "min": "10", "max": "50"}),
        }

class AddEmployee2(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ["material_status", "gender", "phone", "vcation_days", "approved_vacation", "date", "salary"]
        widgets = {
            "material_status": forms.Select(attrs={"id": "materialStatus", "class": "x1", "required": True}),
            "gender": forms.Select(attrs={"id": "gender", "class": "x2", "required": True}),
            "phone": forms.TextInput(attrs={"id": "phoneNum", "class": "x2", "placeholder": "Phone number", "required": True, "pattern": "^01[0-2]\d{1,8}$", "minlength": "11", "maxlength": "11"}),
            "vcation_days": forms.NumberInput(attrs={"id": "vacationNum", "class": "x3", "placeholder": "Vacation days number", "required": True, "min": "1",  "max": "10"}),
            "approved_vacation": forms.NumberInput(attrs={"id": "ApprovedVactions", "class": "x4", "placeholder": "Approved vacation days", "required": True, "min": "0"}),
            "date": forms.DateInput(attrs={"type": "date", "id": "date", "class": "x5", "placeholder": "Date Of Birth", "required": True, "min": "1990-01-01", "max": "2005-12-31"}),
            "salary": forms.NumberInput(attrs={"id": "salary", "class": "x6", "placeholder": "Salary", "required": True, "min": "2000", "max": "6000"})
        }


class EditEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"
        exclude = ['userid']
        widgets = {
            "date": forms.DateInput(attrs={"placeholder": "Date of birth","type":"date"}),
        }

class VacationForm(forms.ModelForm):
    class Meta:
        model = models.Vacation
        fields = ["from_date", "to_date", "Reason"]
        widgets = {
            "from_date": forms.DateInput(attrs={"type": "date", "id": "from-Date", "class": "fD", "required": True}),
            "to_date": forms.DateInput(attrs={"type": "date", "id": "to-Date", "class": "tD", "required": True}),
            "Reason": forms.Textarea(attrs={"id": "Reason", "class": "rs", "placeholder": "Enter The Reason", "cols": "30", "rows": "5", "required": True}),
        }
    

