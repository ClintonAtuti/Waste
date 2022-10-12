import email
from itertools import product
from pickle import TRUE
from sre_constants import CATEGORY
from telnetlib import STATUS
from unicodedata import category, name
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY= (
        ('New', 'New'),
        ('Old', 'Old'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=TRUE)
    category= models.CharField(max_length=200, null=True, choices=CATEGORY)
    descrption= models.CharField(max_length=200, null=True)
    datecreated= models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for deliverly', 'Out for deliverly'),
        ('Deliverly', 'Deliverly'),
    )


    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product =models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
    

