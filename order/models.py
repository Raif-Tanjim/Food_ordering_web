from django.db import models
import random
from random import randint
from Products.models import Product
from Accounts.models import CustomUser
import uuid


class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    Status_CHoices = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'DELIVERED')
    )
    first_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=100, default='', blank=True)
    phone_number = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100,default='',blank=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(null=True, blank=True)
   
    payment_intent = models.CharField(max_length=300)
    used_coupon= models.CharField(max_length=65, blank=True, null=True)
    
    shipped_date = models.DateTimeField(null=True, blank= True)
    delivered_date = models.DateTimeField(null=True, blank= True)
    status = models.CharField(max_length=20, choices= Status_CHoices, default= ORDERED)
   
    def __str__(self):
        return str(self.order_id)
    
    
class OrderItem(models.Model):
    order_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order=models.ForeignKey(Order,related_name='item',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='item',on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.order_item_id)