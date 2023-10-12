from django.conf import settings
from django.db import models

from courses.models import Course, Lesson


class Payment(models.Model):
    """
    Класс для создания платежей
    """
    PAYMENT_CASHLESS = 'безналичная'
    PAYMENT_CASH = 'наличная'

    PAYMENT_CHOICES = (
        (PAYMENT_CASHLESS, 'безналичная'),
        (PAYMENT_CASH, 'наличная')
    )

    payment_date = models.DateField(verbose_name='Дата оплаты')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='тип оплаты')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, verbose_name='урок')

    payment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='плательщик',
                                     null=True, blank=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.payment_date} - {self.payment_amount} - {self.payment_user}'

    class Meta:
        verbose_name = 'Платеж'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Платежи'  # Настройка для наименования набора объектов
        ordering = ('payment_date',)  # сортировка


class Product(models.Model):
    """
    Модель продукта для оплаты
    """
    product_name = models.CharField(max_length=100, verbose_name='продукт')
    product_price = models.IntegerField(default=0, verbose_name='цена')  # cents

    def __str__(self):
        return self.product_name

    def get_display_price(self):
        return "{0:.2f}".format(self.product_price / 100)


class PayStripe(models.Model):
    """
    Модель для создания платежа в системе Stripe
    """
    stripe_id = models.CharField(max_length=255, unique=True, editable=False, verbose_name='id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    customer_email = models.EmailField(null=True, blank=True, verbose_name='почта')
