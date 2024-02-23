from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        default=True,
    )
    name = models.TextField(
        "Название",
        max_length=150,
        help_text="Максимум 150 символов",
        unique=True,
    )

    class Meta:
        abstract = True
