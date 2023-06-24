from django.core.validators import MinLengthValidator
from django.db import models

from FinalExam.validators.user_name_validator import check_first_letter


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIN_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    PASSWORD_MAX_LENGTH = 20
    PASSWORD_MIN_LENGTH = 8
    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            check_first_letter,
        ),
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            check_first_letter,
        ),
        blank=False,
        null=False,
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        validators=(
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        default=DEFAULT_AGE,
        blank=True,
        null=True,
    )
