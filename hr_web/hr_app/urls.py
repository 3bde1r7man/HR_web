from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('home/', views.home, name= "home"),
    path('addEmp/',views.addEmp1 ,name='add'),
    path('addEmp2/',views.addEmp2,name='add2'),
    path('employees/<pk>/update', views.UpdateEmployeeView.as_view(), name= "edit"),
    path('employees/<pk>/delete',views.DeleteEmployeeView.as_view(), name= "delete"),
    path('search/', views.search, name= "search"),
    path('approve_vacation/<int:pk>/', views.approve_vacation, name='approve_vacation'),
    path('reject_vacation/<int:pk>/', views.reject_vacation, name='reject_vacation'),
    path('form/<int:pk>/', views.vacation_form, name= "form"),
    path('request/', views.vacation_request, name= "request"),
]