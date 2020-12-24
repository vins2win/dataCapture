from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=256)

class ItemCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_type = models.CharField(max_length=32)
    manufacturer = models.CharField(max_length=64, blank=True, null=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    manufacturing_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    ingredients = models.CharField(max_length=128, blank=True, null=True)
    allergens = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.CharField(max_length=128, blank=True, null=True)
    images = models.JSONField()
