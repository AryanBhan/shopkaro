from django.shortcuts import HttpResponseRedirect, redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product
class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'login.html')
    def post(self,request):
        postd=request.POST
        email=postd.get('email')
        password=postd.get('password')
        try:
            customer=Customer.objects.get(email=email)
        except:
            customer=False

        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['customer_email']=customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('home')
            else:
                error_message='Email or Password incorrect'
        else:
            error_message="User Doesn't Exist"
        return render(request,'login.html',{'error':error_message})