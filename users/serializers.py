from rest_framework import serializers

from payment.models import Payment
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели User
    """
    payments = serializers.SerializerMethodField()  # данные о платежах пользователя

    class Meta:
        model = User
        fields = '__all__'
        # fields = ('user_email', 'user_phone', 'user_avatar', 'user_city', 'is_active', 'payments')

    def get_payments(self, user):
        """
        Метод определения поля payments
        :return: список платежей пользователя
        """
        # выводит только суммы платежа
        # payments = [payment.payment_amount for payment in Payment.objects.filter(payment_user=user)]

        payments = []  # задаем список платежей

        for payment in Payment.objects.filter(payment_user=user):  # перебираем все платежи пользователя
            pay = [payment.payment_date, payment.payment_amount]  # список с датой и суммой платежа
            payments.append(pay)  # добавляем каждый платеж в общий список

        return payments
