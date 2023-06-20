from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.validators.plant_validators import is_alpha_check


class Plant(models.Model):
    CHOICES = (
        ('Outdoor', 'Outdoor Plants'),
        ('Indoor', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        max_length=14,
        choices=CHOICES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            is_alpha_check,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ("id",)
