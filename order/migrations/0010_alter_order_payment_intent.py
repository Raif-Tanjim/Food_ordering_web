# Generated by Django 5.0.1 on 2024-01-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='5a7a5188-866a-4b08-8cde-1b68e5e56b0e', max_length=100),
        ),
    ]
