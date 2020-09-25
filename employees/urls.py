from django.contrib import admin
from django.urls import path
from .views import AddEmployee,EmployeeView,search,index,DeleteEmployee,EditEmployees
urlpatterns=[
    path('',index,name='employees'),
    # path('<int:employee_id>',views.employees,name='employee'),
    path('add-employee/',AddEmployee.as_view(),name='addemployee'),
    path('view-employee/',EmployeeView.as_view(), name='viewemployee'),
    path('delete-employee/<int:id>', DeleteEmployee, name='deleteemployee'),
    path('edit-employee/<int:id>', EditEmployees, name='editemployee'),

    path('search/',search,name='searchemployee'),
]