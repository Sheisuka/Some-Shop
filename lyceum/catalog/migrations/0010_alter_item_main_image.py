# Generated by Django 4.2.1 on 2024-02-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="main_image",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_main",
                to="catalog.image",
                verbose_name="главное изображение",
            ),
        ),
    ]
