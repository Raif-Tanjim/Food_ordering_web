# Generated by Django 4.2.4 on 2023-09-01 11:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('update_at', models.DateField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('update_at', models.DateField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_measuring', models.CharField(blank=True, choices=[('ML', 'ML'), ('KG', 'KG'), ('L', 'L')], max_length=100, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('is_restrict', models.BooleanField(default=True)),
                ('restrict_quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='Products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('update_at', models.DateField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_Image', models.ImageField(upload_to='Products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
