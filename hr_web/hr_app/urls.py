from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('home/', views.home, name= "home"),
    path('addEmp/', views.add, name= "add"),
    path('addEmp2/', views.add2, name= "add2"),
    path('search/', views.search, name= "search"),
    path('edit/', views.edit, name= "edit"),
    path('form/', views.vacation_form, name= "form"),
    path('request/', views.vacation_request, name= "request"),

]