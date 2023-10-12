import requests
import stripe
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stripe.error import StripeError

from config import settings
from config.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from payment.models import Product, PayStripe

public_token = STRIPE_PUBLIC_KEY
stripe.api_key = STRIPE_SECRET_KEY

card_visa_number = '4242424242424242'
card_visa_cvc = '123'
card_visa_date = '10/25'


@api_view(['POST'])
def test_payment_create(request):

    product = Product.objects.last()

    payment_intent = stripe.PaymentIntent.create(
        amount=product.product_price,
        currency='USD',
        payment_method_types=['card'],
        receipt_email='test@example.com')

    a = JsonResponse({
        'id': payment_intent.id
    })
    response = Response(status=status.HTTP_200_OK, data=payment_intent)

    PayStripe.objects.create(
        stripe_id=payment_intent.id,
        product=product,
    )

    return response


@api_view(['GET'])
def test_payment_detail(request):

    pay_stripe = PayStripe.objects.last()

    payment_detail = stripe.PaymentIntent.retrieve(
        id=pay_stripe.stripe_id
        )

    # a = JsonResponse({
    #     'id': test_payment_intent.id
    # })
    response = Response(status=status.HTTP_200_OK, data=payment_detail)

    return response
