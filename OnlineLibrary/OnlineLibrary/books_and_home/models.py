from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image = models.URLField(
        blank=False,
        null=False,
    )

    type = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['id']
