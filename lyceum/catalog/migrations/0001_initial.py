# Generated by Django 4.2.1 on 2024-02-23 19:25

import catalog.models
import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опубликовано"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        help_text="Максимум 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=200, unique=True, verbose_name="Слаг"
                    ),
                ),
                (
                    "weight",
                    models.PositiveSmallIntegerField(
                        default=100,
                        help_text="Вес должен быть больше нуля и меньше 32767",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(32767),
                        ],
                        verbose_name="Вес",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опубликовано"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        help_text="Максимум 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=200, unique=True, verbose_name="Слаг"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Опубликовано"
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        help_text="Максимум 150 символов",
                        max_length=150,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text='Описание должно содержать слова "роскошно" или "превосходно"',
                        validators=[catalog.validators.gorgeous_validator],
                        verbose_name="Текст",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=catalog.models.Category.get_default_pk,
                        help_text="Выберите категорию",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="catalog.category",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        help_text="Выберите теги",
                        related_name="items",
                        to="catalog.tag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
