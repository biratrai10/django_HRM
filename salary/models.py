from django.db import models
from datetime import datetime
# Create your models here.
class Salary(models.Model):

    sal_job=models.CharField(max_length=200,unique=True)
    sal_type = models.CharField(max_length=200)
    sal_amt = models.FloatField(verbose_name="Enter Amount")
    sal_description = models.TextField(blank=True)

    def __str__(self):
        return self.sal_job


