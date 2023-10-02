from django.urls import path

from payment.apps import PaymentConfig
from rest_framework.routers import DefaultRouter

from payment.views import PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView

app_name = PaymentConfig.name

router = DefaultRouter()

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_change'),
    ] + router.urls
