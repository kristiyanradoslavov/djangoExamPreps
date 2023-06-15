import re

from django.core.exceptions import ValidationError


def username_validator(username):
    pattern = r"^[a-zA-Z0-9_]+$"
    if not re.match(pattern, username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
