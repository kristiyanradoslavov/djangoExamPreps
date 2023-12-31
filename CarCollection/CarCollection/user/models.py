from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2, "The username must be a minimum of 2 chars"),
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(18),
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
