import json
from django.shortcuts import render
from .cart import Cart

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
        'productsstring': json.dumps(products)  # Convert the list of dictionaries to a JSON array
    }
    return render(request, 'cart.html', context)
