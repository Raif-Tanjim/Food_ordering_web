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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Products.views import *
from Accounts.views import *
from .views import *
from Cart.views import *
from Cart.weebhook import webhook
from Products.api import api_add_to_cart,api_remove_from_cart,api_checkout,create_checkout_session
from coupon.api import api_can_use

urlpatterns = [
    path('admin', admin.site.urls),
    path('', home, name = 'home'),
    path('product', products, name='product'),
    path('cart', cart_details, name= 'cart'),
    path('sign-up', sign_up, name ='sign_up'),
    path('login', login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('about', About, name='about'),
    path('profile', profile, name='profile'),
    path('cart/success', success, name='success'),
    path('hooks', webhook, name='webhook'),

 #Store   
    path('<slug:category_slug>/<slug:slug>', Product_details_view, name='Product_details_view'),
    path('<slug:slug>', category_detail, name='category_detail' ),
#Api
    path('Products/api/create_checkout_session', create_checkout_session , name='create_checkout_session'),
    path('Products/api/api_add_to_cart', api_add_to_cart , name='api_add_to_cart'),
    path('Products/api/api_remove_from_cart', api_remove_from_cart,name='api_remove_from_cart'),
    path('Products/api/api_checkout', api_checkout , name='api_checkout'),
    path('coupon/api/api_can_use/', api_can_use , name='api_can_use'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
