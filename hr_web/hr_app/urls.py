from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name= "index"),
    path('home/', views.HomeView.as_view(), name= "home"),
    path('employees', views.EmployeeListView.as_view(), name= "search"),
    path('employees/add', views.AddEmployeeView.as_view(), name= "add"),
    path('employees/continue', views.AddEmployee2View.as_view(), name= "add2"),
    path('employees/<pk>/update', views.UpdateEmployeeView.as_view(), name= "edit"),
    path('employees/<pk>/delete',views.DeleteEmployeeView.as_view(), name= "delete"),
    path('employees/<pk>/submit-vacation', views.vacation_form, name= "submit_vacation"),
    path('employees/vacations', views.vacation_request, name= "request"),

]