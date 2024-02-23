from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
    )
    name = models.TextField(
        max_length=150,
        verbose_name="Название",
        help_text="Максимум 150 символов",
    )

    class Meta:
        abstract = True
