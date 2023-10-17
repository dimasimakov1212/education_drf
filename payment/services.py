import requests
import stripe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from config.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from payment.models import Product, PayStripe

public_token = STRIPE_PUBLIC_KEY
stripe.api_key = STRIPE_SECRET_KEY

# card_visa_number = '4242424242424242'
# card_visa_cvc = '123'
# card_visa_date = '10/25'


@api_view(['POST'])
def stripe_product_create(request):
    """ Создаем продукт для stripe """

    product = Product.objects.get(id=1)  # получаем продукт для оплаты

    # создаем продукт в stripe
    payment_product = stripe.Product.create(
        name=product.product_name
    )

    # получаем ответ от stripe
    response = Response(status=status.HTTP_200_OK, data=payment_product)

    # сохраняем полученный id продукта из stripe
    product.stripe_name_id = payment_product.id
    product.save()

    return response


@api_view(['POST'])
def stripe_price_create(request):
    """ Создаем стоимость для stripe """

    product = Product.objects.get(id=1)  # получаем продукт для оплаты

    # создаем стоимость продукта в stripe
    payment_price = stripe.Price.create(
        unit_amount=product.product_price,
        currency="usd",
        product=product.stripe_name_id,
    )

    # получаем ответ от stripe
    response = Response(status=status.HTTP_200_OK, data=payment_price)

    # сохраняем полученный id стоимости из stripe
    product.stripe_price_id = payment_price.id
    product.save()

    return response


@api_view(['POST'])
def stripe_pay_url_create(request):
    """ Создаем ссылку для оплаты в stripe """

    product = Product.objects.get(id=1)  # получаем продукт для оплаты

    # создаем ссылку для оплаты в stripe
    payment_url = stripe.PaymentLink.create(
        line_items=[
            {
                "price": product.stripe_price_id,
                "quantity": 1,
            },
        ],
    )

    # получаем ответ от stripe
    response = Response(status=status.HTTP_200_OK, data=payment_url)

    # сохраняем объект для оплаты
    PayStripe.objects.create(
        stripe_payment_link_id=payment_url.id,
        product=product,
        stripe_payment_link=payment_url.url
    )

    return response


@api_view(['POST'])
def stripe_payment_intent_create(request):

    product = Product.objects.get(id=1)

    stripe_payment = stripe.PaymentIntent.create(
        amount=product.product_price,
        currency="usd",
        payment_method_types=['card'],
    )

    response = Response(status=status.HTTP_200_OK, data=stripe_payment)

    PayStripe.objects.create(
        product=product,
        stripe_payment_id=stripe_payment.id
    )

    return response


@api_view(['GET'])
def stripe_payment_intent_detail(request):

    payment = PayStripe.objects.get(id=3)

    payment_detail = stripe.PaymentIntent.retrieve(
        payment.stripe_payment_id
    )

    response = Response(status=status.HTTP_200_OK, data=payment_detail)

    return response
