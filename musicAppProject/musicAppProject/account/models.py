from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from musicAppProject.validators.account_validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            username_validator
        ),
        blank=False,
        null=False
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

