from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=30)
    location =models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices =(("IT","IT"),("Non IT", "non IT "),("mobiles phone" ,"mobile phone" )))

  
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    company = models.ForeignKey(Company,on_delete =models.PROTECT)



