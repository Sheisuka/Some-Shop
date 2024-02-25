import re

import django.core.exceptions


WORDS_REGEX = re.compile(r"\w+|\W+")


def gorgeous_validator(value):
    words = set(WORDS_REGEX.findall(value.lower()))

    if not words.intersection({"превосходно", "роскошно"}):
        raise django.core.exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )


class ValidateMustContain:
    def __init__(self, *words, message=None):
        self.words_to_contain = words
        self.message = (
            message
            or f"Должно содержаться одно из слов: \n\t{' '.join(words)}"
        )

    def __call__(self, value):
        value_splitted = set(value.split())
        for word in self.words_to_contain:
            if word in value_splitted:
                return

        raise django.core.exceptions.ValidationError(self.message)
