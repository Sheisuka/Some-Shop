import django.db


__all__ = ["AbstractModel"]


class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        verbose_name="опубликовано",
        default=True,
    )
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        help_text="Максимум 150 символов",
        unique=True,
    )

    class Meta:
        abstract = True
