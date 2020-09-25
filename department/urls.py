from django.contrib import admin
from django.urls import path
from .views import Department,DepartmentView,DeleteDepartments,EditDepartments
urlpatterns=[
    path('add-department/',Department.as_view(), name='adddepartment'),
    path('view-department/',DepartmentView.as_view(), name='viewdepartment'),
    path('delete-department/<int:id>', DeleteDepartments, name='deletedepartments'),
    path('edit-department/<int:id>', EditDepartments, name='editdepartments'),

]