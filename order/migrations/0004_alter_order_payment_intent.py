# Generated by Django 5.0.1 on 2024-01-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='c6f787d7-5e5f-4cda-8064-41efe564fc6c', max_length=100),
        ),
    ]
