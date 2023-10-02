from django.shortcuts import render
from rest_framework import generics

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """
    класс для вывода списка платежей на основе generics
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


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
