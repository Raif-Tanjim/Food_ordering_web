# Generated by Django 4.2.4 on 2023-09-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
