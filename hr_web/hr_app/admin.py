from django.contrib import admin

from .models import Employee, Vacation
# Register your models here.
admin.site.register(Employee)
admin.site.register(Vacation)
