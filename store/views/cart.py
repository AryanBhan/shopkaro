from django.views import View


from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product
class cart(View):
    def get(self,request):
        
        id=list(request.session.get('cart').keys())
        products=Product.get_product_by_list(id)
        print(products)
        return render(request,"cart.html",{'products':products})