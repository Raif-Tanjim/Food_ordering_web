# Generated by Django 4.2.4 on 2023-10-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_rename_price_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0),
        ),
    ]
