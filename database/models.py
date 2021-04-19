from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50)

class Item(models.Model):
    name     = models.CharField(max_length=100)
    price    = models.PositiveIntegerField() 
    stock    = models.PositiveSmallIntegerField()
    date_add = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    category_id = models.PositiveIntegerField()

class Sales(models.Model):
    product_id = models.PositiveIntegerField()
    quantity   = models.PositiveSmallIntegerField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    addition_note = models.TextField(null=True, blank=True)