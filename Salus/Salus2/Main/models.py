from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Company(models.Model):
    name =models.CharField(max_length=200,null=True, blank =True)

    def __str__(self):
        return self.name

    
class Studyinformation(models.Model):
    company_id =models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    business_unit =models.CharField(max_length=2000,null=True,blank=True) 
    facility =models.CharField(max_length=2000,null=True,blank=True) 
    project_id=models.IntegerField(null=True,blank=True,unique=True)
    project_name=models.CharField(max_length=2000,null=True,blank=True,unique=True)
    start_date =models.DateField()
    end_date =models.DateField()
    doc_name =models.CharField(max_length=2000,null=True,blank=True)
    scope =models.CharField(max_length=2000,null=True,blank=True)
    objective=models.CharField(max_length=2000,null=True,blank=True)


    def __str__(self):
        return self