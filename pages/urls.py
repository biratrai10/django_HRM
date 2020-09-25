from django.contrib import admin
from django.urls import path
from .views import LoginView,home,about,signup,dashboard
urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('login/',LoginView.as_view(),name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),

]