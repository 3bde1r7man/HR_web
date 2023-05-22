from django import forms
from . import models

class EditEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"
        exclude = ['userid']
        widgets = {
            "date": forms.DateInput(attrs={"placeholder": "Date of birth","type":"date"}),
        }