from django.core.validators import MinValueValidator
from django.db import models

from musicAppProject.album.utils import get_all_available_genres, floor_float_number


class Album(models.Model):
    available_choices = get_all_available_genres()

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        default=None
    )

    genre = models.CharField(
        max_length=30,
        choices=available_choices,
        blank=False,
        null=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            # floor_float_number,
            MinValueValidator(0.0),
        ),
        blank=False,
        null=False,
    )
