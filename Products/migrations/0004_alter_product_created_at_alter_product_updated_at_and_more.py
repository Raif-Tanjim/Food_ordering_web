# Generated by Django 4.2.4 on 2023-09-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_productmetainformation_product_measuring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productmetainformation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productmetainformation',
            name='product_measuring',
            field=models.CharField(blank=True, choices=[('KG', 'Kilogram'), ('ML', 'Milliliter'), ('L', 'Liter')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productmetainformation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
