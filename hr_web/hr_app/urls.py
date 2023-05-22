from django.urls import path
from . import views
from .views import EmployeeView


urlpatterns = [
    path('', views.index, name= "index"),
    path('home/', views.home, name= "home"),
    path('addEmp/',EmployeeView.as_view(),name='add_employee'),
    path('addEmp2/',EmployeeView.as_view(),name='add_employee2'),
    path('search/', views.search, name= "search"),
    path('employees/<pk>/update', views.UpdateEmployeeView.as_view(), name= "edit"),
    path('employees/<pk>/delete',views.DeleteEmployeeView.as_view(), name= "delete"),
    path('form/<int:pk>/', views.vacation_form, name= "form"),
    path('request/', views.vacation_request, name= "request"),
]