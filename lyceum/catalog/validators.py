import django.core.exceptions


def item_text_validator(value):
    words = value.split()
    if not ("превосходно" in words or "роскошно" in words):
        raise django.core.exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )
