from rest_framework import serializers

from payment.models import Payment, Product, PayStripe


class PaymentSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Payment
    """
    class Meta:
        model = Payment
        # fields = ('payment_date', 'payment_amount', 'payment_type', 'course',)
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Product
    """
    class Meta:
        model = Product

        fields = '__all__'
