from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Payment
    """
    class Meta:
        model = Payment
        # fields = ('lesson_title', 'lesson_description',)
        fields = '__all__'
