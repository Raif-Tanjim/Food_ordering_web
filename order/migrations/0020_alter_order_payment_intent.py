# Generated by Django 5.0.1 on 2024-01-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_alter_order_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, default='8d228d7d-6598-4094-9f83-589f39ac79dd', max_length=100),
        ),
    ]
