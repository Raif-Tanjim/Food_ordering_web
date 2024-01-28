# Generated by Django 5.0.1 on 2024-01-12 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Products.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_price', models.FloatField(default=1)),
                ('is_featured', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Products.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='Products.product')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_image', models.ImageField(upload_to='Products')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_measuring', models.CharField(blank=True, choices=[('KG', 'Kilogram'), ('ML', 'Milliliter'), ('L', 'Liter')], max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('is_restrict', models.BooleanField(default=True)),
                ('restrict_quantity', models.IntegerField()),
                ('title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='Products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
