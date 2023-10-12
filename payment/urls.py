from django.urls import path

from payment import services
from payment.apps import PaymentConfig
from rest_framework.routers import DefaultRouter

from payment.services import test_payment_create, test_payment_detail
from payment.views import PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentRetrieveAPIView, \
    PaymentDestroyAPIView, ProductCreateAPIView, ProductListAPIView

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
    path('pay_create/', test_payment_create, name='pay_create'),
    path('payment_detail/', test_payment_detail, name='payment_detail'),
    ] + router.urls
