# Generated by Django 5.0.1 on 2024-01-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='8d416e4d-02a5-4681-9ac4-f6b9b79eca0e', max_length=100),
        ),
    ]