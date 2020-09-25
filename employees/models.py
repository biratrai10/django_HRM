from django.db import models
from datetime import datetime
from department.models import Department
from salary.models import Salary
# Create your models here.
class Employee(models.Model):
    department=models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='department')
    name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="Enter your email",unique=True)
    address = models.CharField(max_length=200)
    contact_no=models.CharField(max_length=100,verbose_name="Contact_Number",unique=True)
    image = models.ImageField(upload_to='media/', null=True)
    is_active=models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)
    salary=models.ForeignKey(Salary, on_delete=models.DO_NOTHING,related_name='salary')

    def __str__(self):
        return self.name

