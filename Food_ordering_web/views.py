from django.shortcuts import render
from Products.models import *


def home(request):
    products = Product.objects.filter(is_featured =True)
    context = {'products': products}
    return render(request, 'home.html', context)



def About(request):
    return render(request,'about.html')