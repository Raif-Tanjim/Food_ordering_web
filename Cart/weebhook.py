import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .cart import Cart
from order.models import Order


@csrf_exempt
def webhook(request):
    payload = request.body
    event = None

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)


    if event.type == 'checkout.session.completed':
        session = event.data.object
        print(session)
        # Access the PaymentIntent ID from the session
        payment_intent_id = session.get('id')


        if payment_intent_id:
            # Use the payment_intent_id to update your order
            try:
                order = Order.objects.get(payment_intent=payment_intent_id)
                print('payment_intent matched')
                order.paid = True
                order.save()

            except Order.DoesNotExist:
                print('Order not found for PaymentIntent ID: %s', payment_intent_id)
        else:
            print('PaymentIntent ID not present in the session.')

    return HttpResponse(status=200)
