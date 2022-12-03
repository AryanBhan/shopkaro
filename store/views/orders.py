import imp
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models.orders import Order
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
class OrderView(View):
    
    def get(self,request):
        customer=request.session.get('customer_id')
        order=Order.get_order_by_customer(customer)
        
        return render(request,'orders.html',{'order':order})
    
