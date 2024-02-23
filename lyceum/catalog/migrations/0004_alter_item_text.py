# Generated by Django 4.2.1 on 2024-02-23 15:24

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_category_weight_alter_item_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="text",
            field=models.TextField(
                help_text='Описание должно содержатьслова "роскошно" или "превосходно"',
                validators=[catalog.models.item_text_validator],
                verbose_name="Текст",
            ),
        ),
    ]
