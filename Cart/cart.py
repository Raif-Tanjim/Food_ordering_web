from django.conf import settings
from Products.models import Product



class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
        
    def __iter__(self):
        product_ids = self.cart.keys()
        product_clean_ids= []
        
        for product in product_ids:
            product_clean_ids.append(product)
            
            self.cart[str(product)]['product']= Product.objects.get(pk=product)
            
        for item in self.cart.values():
            item['Total_price']= float(item['product_price']) *int(item['quantity']) 
            
            yield item
            
    def __len__(self):
       
        return sum(item['quantity'] for item in self.cart.values())
        
        
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        product_price = product.product_price  # Assign product_price here.

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'product_price': product_price, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1

        self.save()
    def remove(self, product_id):
        if product_id in self.cart:
            print(product_id)
            del self.cart[product_id]
            self.save()
                    
        
    def save(self):
        self.session[settings.CART_SESSION_ID]= self.cart  
        self.session.modified = True