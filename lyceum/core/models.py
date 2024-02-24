import django.db


class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = django.db.models.TextField(
        "название",
        max_length=150,
        help_text="Максимум 150 символов",
        unique=True,
    )

    class Meta:
        abstract = True
