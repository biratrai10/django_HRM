from django.urls import path
from .views import SalaryView,AddSalary,DeleteSalary,EditSalary
urlpatterns=[
    path('add-salary/', AddSalary.as_view(), name='addsalary'),
    path('view-salary/',SalaryView.as_view(),name='viewsalary'),
    path('delete-salary/<int:id>', DeleteSalary, name='deletesalary'),
    path('edit-salary/<int:id>', EditSalary, name='editsalary'),

]