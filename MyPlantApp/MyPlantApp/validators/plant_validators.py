from django.core.exceptions import ValidationError


def is_alpha_check(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


