
from datetime import datetime
from email.policy import default
from statistics import mode
from tkinter import CASCADE
from django.db import models
from .product import Product
from .customer import Customer

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.today)
    phno=models.CharField(max_length=13,default="9419102342")
    address=models.CharField(max_length=500,default="New,Delhi")
    status=models.BooleanField(default=False)
    def placeOrder(self):
        self.save()
    # def __str__(self) -> str:
    #     return self.product
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('date')