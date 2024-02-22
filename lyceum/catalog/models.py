from django.db import models
from django.core import exceptions, validators

from Core.models import AbstractModel


def item_text_validator(value):
    if not ("превосходно" in value.lower() or "роскошно" in value.lower()):
        raise exceptions.ValidationError(
            'В тексте должно содержаться "роскошно" или "превосходно"'
        )


class Tag(AbstractModel):
    slug = models.SlugField(verbose_name="Слаг", max_length=200)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Category(AbstractModel):
    slug = models.SlugField(verbose_name="Слаг", max_length=200)
    weight = models.PositiveSmallIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(32767),
        ],
        default=100,
        verbose_name="Вес",
        help_text="Вес должен быть больше нуля и меньше 32767",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(
            name="Другое", defaults=dict(slug="other")
        )
        return category.pk

    def __str__(self):
        return self.name


class Item(AbstractModel):
    text = models.TextField(
        validators=[item_text_validator],
        verbose_name="Текст",
        help_text='Описание должно содержать слова "роскошно" или "превосходно"',
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        default=Category.get_default_pk,
        help_text="Выберите категорию",
    )
    tags = models.ManyToManyField(
        Tag, verbose_name="Тег", help_text="Выберите теги"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
