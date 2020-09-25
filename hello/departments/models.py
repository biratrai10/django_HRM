from django.db import models
from datetime import datetime
# from django.contrib.admin import ModelAdmin as Admin
# Create your models here.



class Department(models.Model):
    title = models.CharField(max_length=200)
    demail = models.EmailField(verbose_name="Enter your email", unique=True)
    daddress=models.CharField(verbose_name="Department Address",max_length=200)
    description = models.TextField(blank=True)
    dcontact = models.CharField(max_length=100, verbose_name="Contact_Number", unique=True)
    # user=models.ForeignKey(Admin,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



