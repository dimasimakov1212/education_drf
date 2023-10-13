import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from rest_framework.filters import OrderingFilter

from payment.models import Payment, Product, PayStripe
from payment.serializers import PaymentSerializer, ProductSerializer


class PaymentListAPIView(generics.ListAPIView):
    """
    класс для вывода списка платежей на основе generics
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('course', 'lesson', 'payment_type')  # Набор полей для фильтрации
    ordering_fields = ['payment_date']


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    класс для создания платежа на основе generics
    """
    serializer_class = PaymentSerializer


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения оплаты на основе generics
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного платежа на основе generics
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления одного мото на основе generics
    """
    queryset = Payment.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    """
    класс для создания продукта для оплаты
    """
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    класс для вывода списка продуктов
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного платежа на основе generics
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления одного мото на основе generics
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# def pay_stripe_create():
#
#     """
#     класс для создания оплаты товара
#     """
#
#     # product = get_object_or_404(Product, pk=self.kwargs['pk'])
#     product = Product.objects.get(id=1)
#
#     amount = product.product_price
#
#     pay_create = test_payment_create(amount)
#
#     # PayStripe.objects.create(
#     #     stripe_id=pay_create.id,
#     #     product=product,
#     # )
#
#     return pay_create
