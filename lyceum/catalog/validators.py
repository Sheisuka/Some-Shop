import django.core.exceptions


def item_text_validator(value):
    if not ("превосходно" in value or "роскошно" in value):
        raise django.core.exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )
