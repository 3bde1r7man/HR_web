from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import AddEmployee1, AddEmployee2,EditEmployee
from .models import Employee
from django.views.generic import UpdateView,TemplateView,FormView,ListView,RedirectView,DeleteView
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(TemplateView):
    template_name = 'projects.html'

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


class EmployeeListView(ListView):
    model = Employee
    template_name ='search.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        query = self.request.GET.get('q','')
        if query:
            return Employee.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query))
        else:
            return Employee.objects.all()

class UpdateEmployeeView(UpdateView):
    model = Employee
    form_class = EditEmployee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

def vacation_form(request):
    return render(request, 'vacation_form.html')

def vacation_request(request):
    return render(request, 'vacation_requests.html')


class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')

    def post(self, *args, **kwargs):
        self.object.delete()
        return HttpResponseRedirect(self.success_url)

