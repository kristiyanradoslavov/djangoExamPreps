from django.core.exceptions import ValidationError


def check_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Fruit name should contain only letters!')
