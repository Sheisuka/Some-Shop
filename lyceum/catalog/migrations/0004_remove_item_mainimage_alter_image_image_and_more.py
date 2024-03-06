# Generated by Django 4.2.1 on 2024-03-06 12:08

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_item_is_on_main"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="MainImage",
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(
                default=None,
                null=True,
                upload_to=catalog.models.item_directory_path,
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="item",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="catalog.item",
                verbose_name="товар",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="is_on_main",
            field=models.BooleanField(
                default=False, verbose_name="находится на главной"
            ),
        ),
        migrations.CreateModel(
            name="MainImage",
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
                    "image",
                    models.ImageField(
                        default=None,
                        null=True,
                        upload_to=catalog.models.item_directory_path,
                        verbose_name="изображение",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="main_image",
                        to="catalog.item",
                        verbose_name="Главное изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "главное изображение",
                "verbose_name_plural": "главные изображения",
            },
        ),
    ]
