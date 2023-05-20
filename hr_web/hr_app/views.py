from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView,TemplateView,FormView,ListView,RedirectView,DeleteView
from .forms import AddEmployee1, AddEmployee2, vacationForm, EditEmployee
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'projects.html')

class AddEmployeeView(FormView):
    form_class = AddEmployee1
    template_name = 'add1.html'
    success_url = reverse_lazy("add2")

    def form_valid(self, form):
        self.request.session['employee_data'] = form.cleaned_data
        return HttpResponseRedirect(self.success_url)


class AddEmployee2View(FormView):
    form_class = AddEmployee2
    template_name = 'add2.html'
    success_url = reverse_lazy("search")

    def get(self, request, *args, **kwargs):
        if 'employee_data' not in self.request.session:
            return redirect('add1')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        employee_data = self.request.session.get('employee_data',{})
        employee_data.update(form.cleaned_data)
        employee = Employee(**employee_data)
        employee.save()
        del self.request.session['employee_data']
        return super().form_valid(form)

def search(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request,'search.html', context=context)

def edit(request):
    return render(request, 'edit.html')

def vacation_form(request, pk=None):
    if pk:
        employee = Employee.objects.get(pk=pk)
        form = vacationForm(initial={'employee': employee.emp_id, 'emp_Name': employee.first_name + ' ' + employee.last_name})
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