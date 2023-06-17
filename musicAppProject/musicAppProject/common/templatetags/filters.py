from django import template

register = template.Library()


@register.filter(name='fixed')
def to_fixed(digit):
    digits_after_decimal_place = 2
    return f"{digit:.{digits_after_decimal_place}f}"

