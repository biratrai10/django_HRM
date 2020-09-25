from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Employee
from employees.models import Employee
from django.contrib.auth import authenticate,login
import datetime
# Create your views here.
def index(request):
    return render(request,'employees/employees.html')

class AddEmployee(LoginRequiredMixin,View):
    template_name = 'employees/add_employee.html'
    login_url = '/login'

    def get(self, request):
            context = {
                'form': EmployeeForm()
            }
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = EmployeeForm( request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Sooryy error occured")
            return redirect('dashboard')

class EmployeeView(LoginRequiredMixin,View):
    template_name = 'employees/employees.html'
    login_url='/login'

    def get(self, request):
        context={
            'employees':Employee.objects.all()
        }

        return render(request, self.template_name,context)

def search(request):
    return render(request,'employees/search.html')

def DeleteEmployee(request, id):
    e = Employee.objects.get(pk=id)
    e.delete()
    messages.add_message(request, messages.SUCCESS, "Successfully Deleted")
    return redirect('viewemployee')

def EditEmployees(request, id):

    data = Employee.objects.get(pk=id)
    form= EmployeeForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Created Successfully")
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'departments/edit_department.html', context)

