import json
from django.conf import settings
from django.shortcuts import render
from .cart import Cart
from order.models import Order

# Create your views here.

def cart_details(request):
    cart = Cart(request)
    products = []

    for item in cart:
        product = item['product']
        product_data = {
            'id': product.id,
            'title': product.title,
            'product_price': product.product_price,
            'quantity': item['quantity'],
            'Total_price': item['Total_price']
        }
        products.append(product_data)

    context = {
        'cart': cart,
        'pub_key':settings.STRIPE_API_KEY_PUBLISHABLE ,
        'productsstring': json.dumps(products)  # Convert the list of dictionaries to a JSON array
    }
    return render(request, 'cart.html', context)
 
def success(request):
    cart = Cart(request)

    cart.clear()

    return render(request,  'success.html')