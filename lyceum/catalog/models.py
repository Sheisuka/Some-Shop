from django.core import exceptions, validators
from django.db import models

from core.models import AbstractModel


def item_text_validator(value):
    if not ("превосходно" in value or "роскошно" in value):
        raise exceptions.ValidationError(
            ('В тексте должно содержаться "роскошно" или "превосходно"'),
        )


class Tag(AbstractModel):
    slug = models.SlugField("Слаг", max_length=200, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Category(AbstractModel):
    slug = models.SlugField("Слаг", max_length=200, unique=True)
    weight = models.PositiveSmallIntegerField(
        "Вес",
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(32767),
        ],
        default=100,
        help_text="Вес должен быть больше нуля и меньше 32767",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

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
        "Текст",
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
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
