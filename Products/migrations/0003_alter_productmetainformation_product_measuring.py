# Generated by Django 4.2.4 on 2023-09-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_productmetainformation_product_measuring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmetainformation',
            name='product_measuring',
            field=models.CharField(blank=True, choices=[('L', 'L'), ('ML', 'ML'), ('KG', 'KG')], max_length=100, null=True),
        ),
    ]
