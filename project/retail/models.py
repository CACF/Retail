from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    contact_information=models.CharField(max_length=15)
    address=models.CharField(max_length=150)

class Order(models.Model):
    order_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    date=models.DateField()
    status=models.CharField(max_length=50)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)



class Supplier(models.Model):
    supplier_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact_information=models.CharField(max_length=15)
    address=models.CharField(max_length=200)


class Product(models.Model):
    product_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    flavour=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    expiry_date=models.DateField()
    order=models.ManyToManyField(Order)
    product_id=models.ForeignKey(Supplier,on_delete=models.CASCADE)

class Distribution_center(models.Model):
    center_id=models.BigAutoField(primary_key=True)
    capacity=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

class Employee(models.Model):
    employee_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact_information=models.CharField(max_length=15)
    address=models.CharField(max_length=200)
    center_id=models.ForeignKey(Distribution_center,on_delete=models.CASCADE)

