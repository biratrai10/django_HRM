from .models import Employee,Salary
from department.models import Department
from salary.models import Salary
from django import forms

class EmployeeForm(forms.ModelForm):
    department=forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_no= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary=forms.ModelChoiceField(queryset=Salary.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))



    class Meta:
        model = Employee
        fields = '__all__'
