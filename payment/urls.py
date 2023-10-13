from django.urls import path

from payment import services
from payment.apps import PaymentConfig
from rest_framework.routers import DefaultRouter

from payment.services import stripe_product_create, stripe_price_create, stripe_pay_url_create, \
    stripe_payment_intent_create, stripe_payment_intent_detail
from payment.views import PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentRetrieveAPIView, \
    PaymentDestroyAPIView, ProductCreateAPIView, ProductListAPIView, ProductDestroyAPIView, ProductRetrieveAPIView

app_name = PaymentConfig.name

router = DefaultRouter()

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment_list'),
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_change'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_detail'),
    path('delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),

    path('product_create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product_list/', ProductListAPIView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('product_delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),

    path('stripe_product_create/', stripe_product_create, name='stripe_product_create'),
    path('stripe_price_create/', stripe_price_create, name='stripe_price_create'),
    path('stripe_pay_url_create/', stripe_pay_url_create, name='stripe_pay_url_create'),
    path('stripe_payment_intent_create/', stripe_payment_intent_create, name='stripe_payment_intent_create'),
    path('stripe_payment_intent_detail/', stripe_payment_intent_detail, name='stripe_payment_intent_detail'),
    ] + router.urls
