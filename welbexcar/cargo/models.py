from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import string


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, related_name='pick_up_location', verbose_name='Локация забора'
        )
    delivery_location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, related_name='delivery_location', verbose_name='Локация доставки'
        )
    weight = models.FloatField(
        verbose_name='Вес',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000)
        ]
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    def __str__(self):
        return self.description


class Car(models.Model):
    def generate_unique_code():
        unique_code = str(random.randint(1000, 9999)) + random.choice(string.ascii_uppercase)
        return unique_code

    def generate_unique_location():
        unique_location = random.choice(Location.objects.all())
        return unique_location

    car_number = models.CharField(
        max_length=5, unique=True, default=generate_unique_code,
        verbose_name='Номер машины'
        )

    current_location = models.ForeignKey(
        'Location', on_delete=models.CASCADE,
        related_name='current_location',
        default=generate_unique_location,
        verbose_name='Текущая локация'
        )

    load_capacity = models.FloatField(
        verbose_name='Грузоподъемность',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000)
        ]
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.car_number


class Location(models.Model):
    city = models.CharField(max_length=200, verbose_name='Город')
    state_name = models.CharField(max_length=200, verbose_name='Штат')
    zip = models.CharField(max_length=10, verbose_name='Почтовый индекс')
    lat = models.CharField(max_length=10, verbose_name='Широта')
    lng = models.CharField(max_length=10, verbose_name='Долгота')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.zip
