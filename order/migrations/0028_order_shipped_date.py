# Generated by Django 5.0.1 on 2024-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
