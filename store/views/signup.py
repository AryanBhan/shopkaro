from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product

class signup(View):

    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postc=request.POST
        fname=postc.get('fname')
        lname=postc.get('lname')
        phno=postc.get('phno')
        email=postc.get('email')
        password=postc.get('password')
        #Validate
        value={
            'fname':fname,
            'lname':lname,
            'phno':phno,
            'email':email
        }
        customer=Customer(fname=fname,lname=lname,phno=phno,email=email,password=password)
        error_message=None
        if (not fname):
            error_message='First name is required'
        elif len(fname)<3:
            error_message='Length of First name must be atleast 3'           
        elif not lname:
            error_message='Enter the Last name'
        elif len(lname)<3:
            error_message='Length of Last name must be atleast 3'                     
        elif not phno:
            error_message="Enter the Phone Number"
        elif len(phno)>12:
            error_message='Phone number must be Upto 12 digit'
        elif not phno.isdigit():
                error_message="Enter the Valid Phone number"
        elif not email:
            error_message='Enter the Email'           
        elif not password:
            error_message='Enter the Password'  
        elif customer.check_email():
            error_message="Email already Exist"       
        if not error_message: 
            customer.password=make_password(customer.password)  
            customer.register()
            return redirect('/')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)