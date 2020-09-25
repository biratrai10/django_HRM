from django import forms
from .models import Salary

class SalaryForm(forms.ModelForm):
    sal_job=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sal_type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sal_amt=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    sal_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Salary
        fields = '__all__'
