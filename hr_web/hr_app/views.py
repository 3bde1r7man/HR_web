from django.contrib import messages
from django.views import View 
from django.views.generic import UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Employee, Vacation
from .forms import EditEmployee
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q

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

class UpdateEmployeeView(UpdateView):
    model = Employee
    form_class = EditEmployee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    
class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'edit.html'
    success_url = reverse_lazy('search')


def search(request):
    query = request.GET.get('query', '').strip()

    query_parts = query.split()
    if len(query_parts) == 2:
        first_name = query_parts[0]
        last_name = query_parts[1]
        employees = Employee.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(firstname__icontains=first_name, lastname__icontains=last_name)
        )
    else:
        employees = Employee.objects.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query)
        )
    context = {'employees': employees}
    return render(request, 'search.html', context=context)

def edit(request):
    return render(request, 'edit.html')

class VacationView:
    def vacation_form(request, pk):
    
        current_user = Employee.objects.get(pk=pk)
        existed_request = Vacation.objects.filter(emp_id=current_user.userid).exists()
        if existed_request:
            error_message = 'You have already submitted a request!'
            return HttpResponseRedirect(reverse('search') + '?' + 'invalid')
        
        context={'current_user':current_user,'fullname':current_user.firstname + ' ' + current_user.lastname}
        
        if request.method == 'POST':
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            reason = request.POST.get('subject')
            status ="Submitted"
            e_id = current_user.userid
            e_name = current_user.firstname + ' ' + current_user.lastname
            data = Vacation(emp_id=e_id, emp_name=e_name, fromDate=from_date, toDate=to_date, reason=reason, status=status, employee=current_user)

            if (from_date >= to_date):
                messages.error(request, 'Please enter a valid date range!')
                return render(request, 'vacation_form.html', context=context)             
            
            data.save()
            messages.success(request, 'Your request has been submitted successfully!')
            return redirect('search')
        
        return render(request, 'vacation_form.html', context=context)


    def vacation_request(request):
        return render(request, 'vacation_requests.html')

    def all_vacations(request):
        vacations = Vacation.objects.values()
        return JsonResponse(list(vacations), safe=False)

    def approve_vacation(request, id):
        if request.method == 'POST':
            employee = get_object_or_404(Employee, pk=id)
            vacation = get_object_or_404(Vacation, emp_id=id)
            from_date = vacation.fromDate
            to_date = vacation.toDate
            diff = (to_date - from_date).days
            days = diff
            if employee.vcation_days >= days:
                employee.vcation_days -= days
                employee.approved_vacation += days
                employee.save()
                vacation.delete()
                return JsonResponse({'message': 'Vacation approved successfully.'})
            else:
                vacation.delete()
                return JsonResponse({'message': 'Invalid number of vacation days.'}, status=400)

    def reject_vacation(request, id):
        if request.method == 'POST':
            vacation = get_object_or_404(Vacation, emp_id=id)
            vacation.delete()
            return JsonResponse({'message': 'Vacation rejected successfully.'})