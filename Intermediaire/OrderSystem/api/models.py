from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_legnth= 100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    

class Order(models.Model):
    STATUS = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
    
    customer = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.CharField(max_length=20, choices= STATUS, default="Pending")
    order_date = models.DateTimeField(auto_now_add=True)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)