from django.urls import path
from . import views
from .views import EmployeeView


urlpatterns = [
    path('', views.index, name= "index"),
    path('home/', views.home, name= "home"),
    path('addEmp/',EmployeeView.as_view(),name='add_employee'),
    path('addEmp2/',EmployeeView.as_view(),name='add_employee2'),
    path('search/', EmployeeView.as_view(), name= "search"),
    path('edit/', views.edit, name= "edit"),
    path('form/', views.vacation_form, name= "form"),
    path('request/', views.vacation_request, name= "request"),
]