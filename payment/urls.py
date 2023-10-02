from django.urls import path

from payment.apps import PaymentConfig
from rest_framework.routers import DefaultRouter

from payment.views import PaymentListAPIView, PaymentCreateAPIView

app_name = PaymentConfig.name

router = DefaultRouter()

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    ] + router.urls
