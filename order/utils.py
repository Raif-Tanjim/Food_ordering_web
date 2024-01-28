from order.models import Order, OrderItem
from Cart.cart import Cart

def checkout(request, first_name, last_name, address, phone_number, city):
    order = Order(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, city=city)
    order.save()
    cart = Cart(request)
    
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['product_price'], quantity=item['quantity'])
    
    return order.order_id
