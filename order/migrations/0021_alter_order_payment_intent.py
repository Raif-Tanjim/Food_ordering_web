# Generated by Django 5.0.1 on 2024-01-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='07ceaebf-3429-4cc4-9432-558261b25b89', max_length=100, null=True),
        ),
    ]
