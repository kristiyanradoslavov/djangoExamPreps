from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.validators.profile_validators import check_first_letter_capital


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=(
            check_first_letter_capital,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=(
            check_first_letter_capital,
        ),
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
