from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
        ),
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
