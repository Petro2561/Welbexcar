# Generated by Django 3.2.19 on 2023-05-28 22:25

import cargo.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0004_auto_20230526_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='current_location',
            field=models.ForeignKey(default=cargo.models.Car.generate_unique_location, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='cargo.location', verbose_name='Текущая локация'),
        ),
    ]
