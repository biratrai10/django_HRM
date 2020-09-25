from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib import messages
# from .models import Salary
from .models import Department
from department.models import Department as DepartmentModel
from django.contrib.auth import authenticate,login
# from .forms import ExpensesCategoryForm,ExpensesForm
from .forms import DepartmentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView
import datetime
from django.urls import reverse_lazy


# Create your views here.
class Department(LoginRequiredMixin,View):
    template_name = 'departments/add_department.html'
    login_url = '/login'

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
    template_name ='departments/view_departments.html'

    login_url='/login'

    def get(self, request):
        context = {
            'department': DepartmentModel.objects.all()
        }
        return render(request, self.template_name, context)

# class DeleteDepartmentView(DeleteView):
#     template_name = '/departments/delete_department.html'
#     success_url = reverse_lazy('viewdepartment')
#     model = Department
#     id_field='id'

def EditDepartments(request, id):

    data = DepartmentModel.objects.get(pk=id)
    form = DepartmentForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Created Successfully")
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'departments/edit_department.html', context)

def DeleteDepartments(request,id):
        d=DepartmentModel.objects.get(pk=id)
        d.delete()
        messages.add_message(request, messages.SUCCESS, "Successfully Deleted")
        return redirect('viewdepartment')

