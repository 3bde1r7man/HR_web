from django.shortcuts import render
from django.contrib import messages
from django.views import View
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

class EmployeeView(View):
        
    def add_employee(self, request): 
        return render(request, 'add1.html')

    def add_employee2(self, request):
        request.session['firstname'] = request.POST.get('firstname')
        request.session['lastname'] = request.POST.get('lastname')
        request.session['email'] = request.POST.get('email')
        request.session['userid'] = request.POST.get('userid')
        request.session['address'] = request.POST.get('address')
        request.session.save()
        return render(request, 'add2.html')
    
    def dispatch(self, request, *args, **kwargs):
        # Call the desired function based on the URL or any other condition
        if request.path == '/addEmp/':
            return self.add_employee(request)
        elif request.path == '/addEmp2/':
            return self.add_employee2(request) 
        elif request.path == '/search/':
            return render(request, 'search.html') 
        else:
            # Call the parent dispatch method to handle other cases
            return super().dispatch(request, *args, **kwargs)
        
def search(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request,'search.html', context=context)

def edit(request):
    return render(request, 'edit.html')

def vacation_form(request):
    return render(request, 'vacation_form.html')

def vacation_request(request):
    return render(request, 'vacation_requests.html')