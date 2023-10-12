# Generated by Django 4.2.5 on 2023-10-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayStripe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(editable=False, max_length=255, unique=True, verbose_name='id')),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='почта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.product', verbose_name='продукт')),
            ],
        ),
    ]
