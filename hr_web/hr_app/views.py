from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

class EmployeeView(View):
    def add_employee(self, request): 
        if request.method == 'POST':
            request.session['firstname'] = request.POST.get('firstname')
            request.session['lastname'] = request.POST.get('lastname')
            request.session['email'] = request.POST.get('email')
            request.session['userid'] = request.POST.get('userid')
            request.session['address'] = request.POST.get('address')
            request.session.save()
            return redirect('add_employee2')
        return render(request, 'add1.html')

    def add_employee2(self, request):
        if request.method == 'POST':
            material_status = request.POST.get('material_status')
            gender = request.POST.get('gender')
            vcation_days = request.POST.get('vcation_days')
            approved_vacation = request.POST.get('approved_vacation')
            phone = request.POST.get('phone')
            salary = request.POST.get('salary')
            date = request.POST.get('date')
            firstname = request.session['firstname']
            lastname = request.session['lastname']
            email = request.session['email']
            userid = request.session['userid']
            address = request.session['address']
            data = Employee(firstname=firstname, lastname=lastname, email=email, userid=userid, address=address, material_status=material_status, gender=gender, phone=phone, vcation_days=vcation_days, approved_vacation=approved_vacation, salary=salary, date=date)
            data.save()
            return redirect('search')
        return render(request, 'add2.html')
    
    def dispatch(self, request, *args, **kwargs):
        # Call the desired function based on the URL or any other condition
        if request.path == '/addEmp/':
            return self.add_employee(request)
        elif request.path == '/addEmp2/':
            return self.add_employee2(request) 
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