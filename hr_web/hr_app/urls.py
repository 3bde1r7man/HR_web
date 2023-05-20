from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('home/', views.home, name= "home"),
    path('employees/add', views.AddEmployeeView.as_view(), name= "add"),
    path('employees/continue', views.AddEmployee2View.as_view(), name= "add2"),
    path('employees/<pk>/update', views.UpdateEmployeeView.as_view(), name= "edit"),
    path('employees/<pk>/delete',views.DeleteEmployeeView.as_view(), name= "delete"),
    path('search/', views.search, name= "search"),
    path('form/<int:pk>/', views.vacation_form, name= "form"),
    path('request/', views.vacation_request, name= "request"),

]