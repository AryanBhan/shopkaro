from itertools import product
from django.views import View
from store.models.orders import Order 

from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password

from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product

class CheckOut(View):
    def post(self,request):
        address=request.POST.get('address')
        phno=request.POST.get('phno')
        if phno.isaplha():
            return redirect("/checkout",{'Alert':1})
        cart=request.session.get('cart')
        customer=request.session.get('customer_id')
        keys=list(cart.keys())
        products=Product.get_product_by_list(keys)
        print(address,phno,products)
        for product in products:
            print(product)
            order=Order(

                product=product,
                customer=Customer(id=customer),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phno=phno

            )
            order.save()
        request.session['cart']={}
        return redirect("/")