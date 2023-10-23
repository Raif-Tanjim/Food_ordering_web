from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import *


def products(request):
    products = Product.objects.all()
    context = { 'products':products,
               }
    return render(request,'Product.html', context )

def Product_details_view(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    context = { 'product':product,
               }
    return render(request, 'product_details.html',context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(parent=None)

    context = {
        'category': category,
        'products': products,
    }
    return render(request,'category_details.html' , context)