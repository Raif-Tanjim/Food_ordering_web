# Generated by Django 5.0.1 on 2024-01-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='cb32095c-567e-4d9a-9805-94ae7b9d5cb5', max_length=100),
        ),
    ]