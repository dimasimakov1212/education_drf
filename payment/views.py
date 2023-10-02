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
