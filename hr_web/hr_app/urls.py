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
    path('form/<int:pk>/', views.VacationView.vacation_form, name= "form"),
    path('request/', views.VacationView.vacation_request, name= "request"),
    path('all_vacations/', views.VacationView.all_vacations, name= "all_vacations"),
    path('approve_vacation/<int:id>/', views.VacationView.approve_vacation, name='approve_vacation'),
    path('reject_vacation/<int:id>/', views.VacationView.reject_vacation, name='reject_vacation'),
]