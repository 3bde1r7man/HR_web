from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

def add(request):
    return render(request, 'add1.html')

def add2(request):
    return render(request, 'add2.html')

def search(request):
    return render(request,'search.html')

def edit(request):
    return render(request, 'edit.html')

def vacation_form(request):
    return render(request, 'vacation_form.html')

def vacation_request(request):
    return render(request, 'vacation_requests.html')