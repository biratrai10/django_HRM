from django.contrib import admin
from django.urls import path
from .views import Department,DepartmentView
urlpatterns=[
    path('add-department/',Department.as_view(), name='adddepartment'),
    path('view-department/',DepartmentView.as_view(), name='viewdepartment'),

]