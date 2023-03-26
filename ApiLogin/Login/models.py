from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings






class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_techincal = models.BooleanField(default=False)
  is_customer = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)


class Customers(models.Model):
    customer = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.customer.username


class Techincals(models.Model):
    techincal = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.techincal.username


class Admin(models.Model):
    admin = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.username



class TechincalProfile(models.Model):
    techincal=models.OneToOneField(Techincals,on_delete=models.CASCADE,default=None)
    identityimage = models.ImageField(upload_to='pic', blank=True, null=True)
    name=models.CharField(max_length=200)
    domin=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=30)
    address=models.CharField(max_length=200)

    def __str__(self):
       return self.name




class CustomerProfile(models.Model):
    customer=models.OneToOneField(Customers,on_delete=models.CASCADE,default=None)
    companname=models.CharField(max_length=150)
    manager=models.CharField(max_length=150)
    technicalmanger=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    phonenumber=models.CharField(max_length=150)
    managermobile=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    website=models.CharField(max_length=150)
    facebook=models.CharField(max_length=150)
    serialnumber=models.CharField(max_length=150)
    logo = models.ImageField(upload_to='pic', blank=True, null=True)
    def __str__(self):
       return self.companname













class orders(models.Model):
    description=models.CharField(max_length=150)
    timeofoccurrance=models.DateTimeField(default=None)
    Frequencyofoccurane=models.IntegerField(default=None)
    RequriedVisit=models.DateTimeField(default=None)
    location=models.CharField(max_length=150,default=None)




class image_orders(models.Model):
    order=models.ForeignKey(orders,on_delete=models.CASCADE)
    problemimage = models.ImageField(upload_to='pic')


class mancontact(models.Model):
    order=models.OneToOneField(orders,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=150,default=None)
    techincal=models.ForeignKey(TechincalProfile,on_delete=models.CASCADE,default=None)
    postion=models.CharField(max_length=150,default=None)
    telephone=models.IntegerField(default=0)
    email=models.EmailField(default=None)




class Devices(models.Model):
    oredr=models.OneToOneField(orders,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=150)
    serialnumber=models.CharField(max_length=150)
    yearofmade=models.CharField(max_length=150)
    deviceimage=models.ImageField(upload_to='pic')
    devicemodel=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    workrate=models.CharField(max_length=150)

    def __str__(self):
        return self.name



