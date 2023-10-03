from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer


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
