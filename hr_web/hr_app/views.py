from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import UpdateView,DeleteView
from .forms import vacationForm, EditEmployee, AddEmployee1, AddEmployee2
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

def addEmp1(request):
    if request.method == 'POST':
        form = AddEmployee1(request.POST)
        if form.is_valid():
            emp_data = form.save(commit=False)
            request.session['emp_data'] = {
                'firstname': emp_data.firstname,
                'lastname': emp_data.lastname,
                'email': emp_data.email,
                'userid': emp_data.userid,
                'address': emp_data.address
            }
            return redirect('add2')
    else:
        form = AddEmployee1()
    context = {'form': form}
    return render(request, 'add1.html', context=context)


def addEmp2(request):
    if request.method == 'POST':
        form = AddEmployee2(request.POST)
        if form.is_valid():
            emp_data = form.save(commit=False)
            empDataP1 = request.session.get('emp_data')
            emp_data.firstname = empDataP1['firstname']
            emp_data.lastname = empDataP1['lastname']
            emp_data.email = empDataP1['email']
            emp_data.userid = empDataP1['userid']
            emp_data.address = empDataP1['address']
            emp_data.save()
            del request.session['emp_data']
            return redirect('search')
    else:
        form = AddEmployee2()
    
    context = {'form': form}
    return render(request, 'add2.html', context=context)


class UpdateEmployeeView(UpdateView):
    model = Employee
    form_class = EditEmployee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context



class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')

    def post(self, *args, **kwargs):
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
    



def search(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request,'search.html', context=context)


def vacation_form(request, pk=None):
    if pk:
        employee = Employee.objects.get(pk=pk)
        form = vacationForm(initial={'employee': employee.userid, 'emp_Name': employee.firstname + ' ' + employee.lastname})
    else:
        form = vacationForm()
    
    if request.method == 'POST' and pk is not None:
        form = vacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    
    context = {'form': form}
    return render(request, 'vacation_form.html', context=context)


def vacation_request(request):
    return render(request, 'vacation_requests.html')


def handler404(request, exception):
    return HttpResponse("404: Page Not Found! ")