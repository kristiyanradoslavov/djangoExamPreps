from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        unique=True,
        max_length=30,
        blank=False,
        null=False,
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ),
        blank=False,
        null=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['id']
