# Generated by Django 5.0.1 on 2024-01-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coupom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=65, unique=True)),
                ('value', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('num_available', models.IntegerField(default=1)),
                ('num_used', models.IntegerField(default=0)),
            ],
        ),
    ]
