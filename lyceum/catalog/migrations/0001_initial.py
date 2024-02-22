# Generated by Django 4.2.1 on 2024-02-22 18:23

import catalog.models
from django.db import migrations, models


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
                    models.TextField(max_length=150, verbose_name="Название"),
                ),
                ("slug", models.SlugField(verbose_name="Слаг")),
                (
                    "weight",
                    models.PositiveSmallIntegerField(
                        default=100, verbose_name="Вес"
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
                    models.TextField(max_length=150, verbose_name="Название"),
                ),
                ("slug", models.SlugField(verbose_name="Слаг")),
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
                    models.TextField(max_length=150, verbose_name="Название"),
                ),
                (
                    "text",
                    models.TextField(
                        validators=[catalog.models.item_text_validator],
                        verbose_name="Текст",
                    ),
                ),
                ("tags", models.ManyToManyField(to="catalog.tag")),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]