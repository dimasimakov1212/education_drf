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

    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
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
