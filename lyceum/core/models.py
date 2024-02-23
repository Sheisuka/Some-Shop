from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = models.TextField(
        "название",
        max_length=150,
        help_text="Максимум 150 символов",
        unique=True,
    )

    class Meta:
        abstract = True
