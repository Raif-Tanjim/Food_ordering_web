import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from Cart.cart import Cart
from .models import Product
from order.utils import checkout
from order.models import Order
import stripe
from django.conf import settings
from coupon.models import Coupon


def create_checkout_session(request):
    data = json.loads(request.body)
    
    #Coupon
    coupon_code = data['coupon_code']
    coupon_value = 0
    if coupon_code != '':
        coupon = Coupon.objects.get(code=coupon_code)
        
        if coupon.can_use():
            coupon_value = coupon.value
            coupon.use()    
    #
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    
    items= []
    
    for item in cart:
        product = item['product']
        price = int(product.product_price * 100) 
        
        if coupon_value > 0:
            price = int(price * (int(coupon_value)/100))
            
        obj = {
            'price_data': {
                'currency': 'bdt',
                'product_data': {
                    'name': product.title,
                },
                'unit_amount': price
            },
            'quantity': item['quantity']
        }
        items.append(obj)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='http://127.0.0.1:8000/cart/success',
            cancel_url='http://127.0.0.1:8000/cart',
        )
        print("Session created successfully:", session)

    except stripe.error.StripeError as e:
        # Handle errors, log details, and return an appropriate response
        print(f"Error creating Checkout Session: {str(e)}")
        return JsonResponse({'error': str(e)})

    
    # Create order
    first_name = data['first_name']
    last_name = data['last_name']
    address = data['address']
    phone_number = data['phone_number']
    city= data['city']
    payment_intent = session['id']

    if payment_intent:
        orderid = checkout(request, first_name, last_name, address, phone_number, city)
        total_price= 0.00
        for item in cart:
            product = item['product']
            total_price = total_price + (float(product.product_price) * float(item['quantity']))

        if coupon_value > 0:
            total_price = total_price * (coupon_value / 100)
            
        order = Order.objects.get(pk=orderid)
        print("Other Data:", first_name, last_name, address, phone_number, city)
        order.payment_intent = payment_intent 
        order.paid_amount= total_price
        order.used_coupon= coupon_code
        order.save()
        print("Session Payment Intent:", payment_intent)
    else:
        # Log an error or handle the case where payment_intent is not available
        print("Error: PaymentIntent not available in the session")

        
    return JsonResponse({'session': session})


def api_checkout(request):
    cart = Cart(request)
    data = json.loads(request.body)
    jsonResponse = {'success': True}
    first_name = data['first_name']
    last_name = data['last_name']
    address = data['address']
    phone_number = data['phone_number']
    city= data['city']

    orderid = checkout(request, first_name, last_name, address, phone_number,city)
    paid =True
    if paid == True:
        order = Order.objects.get(pk=orderid)
        order.paid =True
        order.paid_amount= cart.get_total_cost()
        order.save()
        
        cart.clear()
    return JsonResponse(jsonResponse)

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

    
    