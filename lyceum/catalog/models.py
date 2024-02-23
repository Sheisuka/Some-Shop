from django.core import exceptions, validators
from django.db import models

from core.models import AbstractModel


def item_text_validator(value):
    words = value.split()
    if not ("превосходно" in words or "роскошно" in words):
        raise exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )


class Tag(AbstractModel):
    slug = models.SlugField("слаг", max_length=200, unique=True)

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Category(AbstractModel):
    slug = models.SlugField("слаг", max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(
        "вес",
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(32767),
        ],
        default=100,
        help_text="Вес должен быть больше нуля и меньше 32767",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(
            name="Другое",
            slug="other-slug",
        )
        return category.pk

    def __str__(self):
        return self.name


class Item(AbstractModel):
    text = models.TextField(
        "текст",
        validators=[item_text_validator],
        help_text="Описание должно содержать "
        'слова "роскошно" или "превосходно"',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=Category.get_default_pk,
        help_text="Выберите категорию",
        related_name="items",
    )
    tags = models.ManyToManyField(
        Tag,
        help_text="Выберите теги",
        related_name="items",
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]
