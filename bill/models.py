from django.db import models
from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    username = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, default="avadhoot")
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    DOB = models.DateField()

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name


class UserContact(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.BigIntegerField(max_length=12)


class Login(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    login_date = models.DateField(
        auto_now_add=True)
    login_time = models.TimeField(
        auto_now_add=True)

    def __str__(self):
        return self.username


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(
        max_length=50, blank=True, null=True)
    address = models.CharField(
        max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class CustomerContact(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact = models.BigIntegerField(max_length=12)


class Product(models.Model):
    Product_Name = models.CharField(
        max_length=50, blank=True, null=True)
    Price = models.IntegerField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.Product_Name


class Bill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Quantity = models.IntegerField(max_length=10)
    Amount = models.IntegerField(max_length=15)
