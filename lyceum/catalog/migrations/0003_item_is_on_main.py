# Generated by Django 4.2.1 on 2024-03-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_item_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="is_on_main",
            field=models.BooleanField(
                default=False, verbose_name="Находится на главной"
            ),
        ),
    ]
