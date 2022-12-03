
import imp
from django.contrib import admin
from django.urls import path,include
from store import views
from .views.login import Login
from .views.cart import cart
from .views.signup import signup
from .views.logout import logout
from .views.home import index
from .views.orders import OrderView
from .views.checkout import CheckOut
from .middlewares.auth import auth_middleware
urlpatterns = [
    path("",index.as_view(),name='home'),
    path("order",auth_middleware(OrderView.as_view()),name='order'),
    path("signup",signup.as_view(),name='signup'),
    path("login",Login.as_view(),name='login'),
    path("logout",logout.as_view(),name='logout'),
    path("cart",cart.as_view(),name='cart'),
    path("check-out",CheckOut.as_view(),name='check-out')

]