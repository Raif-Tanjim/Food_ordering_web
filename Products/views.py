from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import *


def products(request):
    products = Product.objects.all()
    context = { 'products':products,
               }
    return render(request,'Product.html', context )

def Product_details_view(request, product_slug):
    products = Product.objects.filter(product_slug=product_slug)
    context = { 'products':products,
               }
    return render(request, 'product_details.html',context)