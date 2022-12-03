from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from store.models import Category
from store.models import Product
from store.models import Customer
from django.views import View
from store.models.product import Product
# Create your views here.
class index(View):
    def post(self,request):    
        product=request.POST.get('product')
        cart=request.session.get('cart')
        remove=request.POST.get('remove')
        
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print('Cart:',request.session['cart'])
        return redirect('/')
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        product=None
        category=Category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
            product=Product.get_all_product_by_catid(categoryID)
        else:
            product=Product.get_all_product()
        data={}
        data['product']=product
        data['category']=category
        print(request.session.get('customer_email'))
        return render(request,'index.html',data)