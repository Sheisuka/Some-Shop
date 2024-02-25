import django.core.validators
import django.db.models

import catalog.validators
import core.models


class Tag(core.models.AbstractModel):
    slug = django.db.models.SlugField("слаг", max_length=200, unique=True)

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Category(core.models.AbstractModel):
    slug = django.db.models.SlugField("слаг", max_length=200, unique=True)
    weight = django.db.models.PositiveSmallIntegerField(
        "вес",
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32767),
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


class Item(core.models.AbstractModel):
    text = django.db.models.TextField(
        "текст",
        validators=[catalog.validators.gorgeous_validator],
        help_text="Описание должно содержать "
        'слова "роскошно" или "превосходно"',
    )
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        default=Category.get_default_pk,
        help_text="Выберите категорию",
        related_name="items",
    )
    tags = django.db.models.ManyToManyField(
        Tag,
        help_text="Выберите теги",
        related_name="items",
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]
