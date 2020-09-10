from django.core.exceptions import ValidationError


def quantityValidator(value):
    if value > 20:
        raise ValidationError(f'{value} is big quantity (max - 20)')
    elif value < 0:
        raise ValidationError(f'{value} can\'t be less 0')
