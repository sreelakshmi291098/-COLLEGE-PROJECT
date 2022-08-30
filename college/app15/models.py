from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Studreg(models.Model):
    Firstname=models.CharField(max_length=264,unique=True)
    Middlename=models.CharField(max_length=264,unique=True)
    Lastname=models.CharField(max_length=264,unique=True)
    Course=models.CharField(max_length=264,unique=True)
    Gender=models.CharField(max_length=264,unique=True)
    Current_Address=models.CharField(max_length=264,unique=True)
    Email=models.CharField(max_length=264,unique=True)
    Password=models.CharField(max_length=264,unique=True)
    conform_Password=models.CharField(max_length=264,unique=True)


class Empreg(models.Model):
    Firstname=models.CharField(max_length=264,unique=True)
    Middlename=models.CharField(max_length=264,unique=True)
    Lastname=models.CharField(max_length=264,unique=True)
    Category=models.CharField(max_length=264,unique=True)
    Gender=models.CharField(max_length=264,unique=True)
    Current_Address=models.CharField(max_length=264,unique=True)
    Email=models.CharField(max_length=264,unique=True)
    Password=models.CharField(max_length=264,unique=True)
    conform_Password=models.CharField(max_length=264,unique=True)


class User(AbstractUser):
    is_admin=models.BooleanField('Is admin',default=False)
    is_customer=models.BooleanField('Is customer',default=False)
    is_employee=models.BooleanField('Is employee',default=False)






