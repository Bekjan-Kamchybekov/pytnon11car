# Generated by Django 5.1.2 on 2024-10-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_kg', '0002_alter_car_fuel_alter_car_steering_wheel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
