import random
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')


class LoginView(View):
    template_name='pages/login.html'

    def get(self,request):
        if request.user.is_authenticated:
             return redirect('dashboard')
        return render(request, self.template_name)

    def post(self,request,*args,**kwargs):

        u=request.POST.get('username')
        p=request.POST.get('pass')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"Login Credentiak doesnt match")
            return redirect('signin')

# def signin(request):
#     return  render(request,'pages/login.html')

def signup(request):
    return  render(request,'pages/signup.html')

def dashboard(request):
    return render(request,'pages/dashboard.html')

