# Generated by Django 4.2.1 on 2024-02-29 20:06

from django.db import migrations, models
import django.db.models.deletion

__all__ = ["Migration"]


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_squashed_0010_alter_item_main_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="main_image",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_main",
                to="catalog.image",
                verbose_name="главное изображение",
            ),
        ),
    ]
