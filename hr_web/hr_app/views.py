from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import AddEmployee1, AddEmployee2,EditEmployee
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

def add(request):
    if request.method == "POST":
        form = AddEmployee1(request.POST)
        if form.is_valid():
            request.session['employee_data'] = form.cleaned_data
            return redirect('add2')
    else:
        form = AddEmployee1()
    context = {'form': form}

    return render(request, 'add1.html',context=context)

def add2(request):
    employee_data = request.session.get('employee_data', {})
    if not employee_data:
        return redirect('add')
    if request.method == "POST":
        form = AddEmployee2(request.POST)
        if form.is_valid():
            employee_data.update(form.cleaned_data)
            employee = Employee(**employee_data)
            employee.save()
            del request.session['employee_data']
            return redirect('search')
    else:
        form = AddEmployee2()
    context = {'form': form}

    return render(request, 'add2.html', context=context)

def search(request):
    return render(request,'search.html')

def edit(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    if request.method == "POST":
        print("posting employee")
        form = EditEmployee(request.POST, instance=employee)
        if form.is_valid() and request.method.get("emp_id")==employee.emp_id:
            form.save()
            return redirect('search')
    elif request.method == "DELETE":
        print("deleting employee")
        employee.delete()
        return redirect('search')
    else:
        form = EditEmployee(instance=employee)
    context = {'form': form,"employee":employee}
    return render(request, 'edit.html',context=context)

def vacation_form(request):
    return render(request, 'vacation_form.html')

def vacation_request(request):
    return render(request, 'vacation_requests.html')