from django.core.validators import MinLengthValidator
from django.db import models

from FinalExam.validators.fruit_name_validator import check_letters


class Fruit(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            check_letters,
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['id']
