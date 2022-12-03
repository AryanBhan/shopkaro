from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product
class logout(View):    
    def get(self,request):
        request.session.clear()
        return redirect("/")