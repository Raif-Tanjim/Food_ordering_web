import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from Cart.cart import Cart
from .models import Product

def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonResponse = {'success': True}
    product_id = str(data['product_id'])
    update = data['update']
    quantity= data['quantity']
    cart = Cart(request)
    
    product = get_object_or_404(Product, pk = product_id)
    
    if not update:
        cart.add(product=product,quantity=quantity,update_quantity=False)
    else:
        cart.add(product=product, quantity= quantity, update_quantity=True)
        
    return JsonResponse(jsonResponse)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonResponse = {'success': True}
    product_id =str(data ['product_id'])
    
    cart = Cart(request)
    cart.remove(product_id)
    return JsonResponse(jsonResponse)

    
    