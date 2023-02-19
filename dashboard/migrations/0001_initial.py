# Generated by Django 4.1.7 on 2023-02-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('total_capacity', models.PositiveIntegerField()),
                ('capacity_occupied', models.PositiveIntegerField()),
                ('capacity_available', models.PositiveIntegerField()),
                ('temperature_control', models.BooleanField()),
                ('last_updated', models.DateField()),
            ],
        ),
    ]