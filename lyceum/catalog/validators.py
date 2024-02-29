import re

import django.core.exceptions
import django.utils.deconstruct

__all__ = ["ValidateMustContain", "gorgeous_validator"]


WORDS_REGEX = re.compile(r"\w+|\W+")


def gorgeous_validator(value):
    words = set(WORDS_REGEX.findall(value.lower()))

    if not words.intersection({"превосходно", "роскошно"}):
        raise django.core.exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *args):
        self.needed_words = {word.lower() for word in args}

    def __call__(self, value):
        words = set(WORDS_REGEX.findall(value.lower()))
        if not self.needed_words.intersection(words):
            joined_needed_words = ", ".join(self.needed_words)
            raise django.core.exceptions.ValidationError(
                "В тексте должно содержаться одно из слов: "
                f"{joined_needed_words}",
            )
