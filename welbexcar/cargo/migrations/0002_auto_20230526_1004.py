# Generated by Django 3.2.19 on 2023-05-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.CharField(max_length=10, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.CharField(max_length=10, verbose_name='Долгота'),
        ),
    ]
