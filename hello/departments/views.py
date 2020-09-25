from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib import messages
# from .models import Salary
from .models import Department
from departments.models import Department
from django.contrib.auth import authenticate,login
# from .forms import ExpensesCategoryForm,ExpensesForm
from .forms import DepartmentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView
import datetime

# Create your views here.
class Department(LoginRequiredMixin,View):
    template_name = 'departments/add_department.html'
    # login_url = '/account/login'

    def get(self, request):
        context = {
            'form': DepartmentForm(),
            # 'department':Department.objects.all(),
            # 'category': Department.objects.filter(user_id=request.user.id),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Sooryy error occured")
            return redirect('dashboard')


class DepartmentView(LoginRequiredMixin,View):
    template_name='departments/view_departments.html'
    # login_url='/account/login'


    def get(self,request):
        print(Department.objects.all())
        context = {
            'depart': Department.objects.all()
        }
        return render(request, self.template_name,context)