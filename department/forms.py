from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    demail=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    daddress=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    dcontact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Department
        fields = '__all__'
