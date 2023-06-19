from django.core.exceptions import ValidationError


def check_first_letter_capital(value):
    first_letter = value[0]

    if first_letter != first_letter.upper():
        raise ValidationError("Your name must start with a capital letter!")


