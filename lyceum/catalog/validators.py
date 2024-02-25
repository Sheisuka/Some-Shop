import re

import django.core.exceptions


WORDS_REGEX = re.compile(r"\w+|\W+")


def gorgeous_validator(value):
    words = set(WORDS_REGEX.findall(value.lower()))

    if not words.intersection({"превосходно", "роскошно"}):
        raise django.core.exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )
