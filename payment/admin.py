from django.contrib import admin
from payment.models import Payment, Product, PayStripe

admin.site.register(Payment)
admin.site.register(PayStripe)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Описывает параметры для вывода таблицы клиентов в админку
    """
    list_display = ('id', 'product_name', 'product_price',)
    list_filter = ('id',)
    search_fields = ('product_name',)
