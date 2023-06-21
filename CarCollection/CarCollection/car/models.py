from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from CarCollection.car.car_validators import validate_year


class Car(models.Model):
    CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        max_length=10,
        choices=CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
            validate_year,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(1),
        ),
        null=False,
        blank=False,
    )
