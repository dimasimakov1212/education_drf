from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Payment
    """
    class Meta:
        model = Payment
        # fields = ('payment_date', 'payment_amount', 'payment_type', 'course',)
        fields = '__all__'
