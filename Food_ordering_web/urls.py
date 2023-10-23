"""
URL configuration for food_order_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Products.views import *
from Accounts.views import *
from .views import *
from Cart.views import *
from Products.api import api_add_to_cart,api_remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('product/', products, name='product'),
     path('cart/', cart_details, name= 'cart'),
    path('sign-up/', sign_up, name = 'sign_up'),
    path('about/', About, name='about'),

 #Store   
    path('<slug:category_slug>/<slug:slug>/', Product_details_view, name='Product_details_view'),
    path('<slug:slug>/', category_detail, name='category_detail' ),
#Api
    path('Products/api/api_add_to_cart/',api_add_to_cart , name='api_add_to_cart'),
    path('Products/api/api_remove_from_cart/',api_remove_from_cart,name='api_remove_from_cart') ,
]
