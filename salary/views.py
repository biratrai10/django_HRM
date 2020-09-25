from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib import messages
from .models import Salary
from salary.models import Salary
from django.contrib.auth import authenticate,login
# from .forms import ExpensesCategoryForm,ExpensesForm
from .forms import SalaryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView
import datetime
# from django.urls import reverse_lazy
# Create your views here.
class AddSalary(LoginRequiredMixin,View):
    template_name = 'salary/add_salary.html'
    login_url = '/login'

    def get(self, request):
        context = {
            'form': SalaryForm(),
            # 'department':Department.objects.all(),
            # 'category': Department.objects.filter(user_id=request.user.id),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SalaryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Saved Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Sooryy error occured")
            return redirect('dashboard')

class SalaryView(LoginRequiredMixin,View):
    template_name='salary/view_salary.html'
    login_url='/login'


    def get(self,request):
        print(Salary.objects.all())
        context = {
            'salary': Salary.objects.all()
        }
        return render(request, self.template_name,context)

def EditSalary(request, id):

    data = Salary.objects.get(pk=id)
    form = SalaryForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Created Successfully")
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'salary/update_salary.html', context)


def DeleteSalary(request, id):
    s = Salary.objects.get(pk=id)
    s.delete()
    messages.add_message(request, messages.SUCCESS, "Successfully Deleted")
    return redirect('viewsalary')