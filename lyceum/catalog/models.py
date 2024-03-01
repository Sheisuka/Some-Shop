import django_ckeditor_5.fields
import django.core.validators
import django.db.models
import django.utils.safestring
import sorl.thumbnail

import catalog.validators
import core.models

__all__ = ["Category", "Image", "Item", "Tag"]


class Tag(core.models.AbstractModel):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Category(core.models.AbstractModel):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        max_length=200,
        unique=True,
    )
    weight = django.db.models.PositiveSmallIntegerField(
        verbose_name="вес",
        validators=[
            django.core.validators.MinValueValidator(1),
            django.core.validators.MaxValueValidator(32767),
        ],
        default=100,
        help_text="Вес должен быть больше нуля и меньше 32767",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(
            name="Другое",
            slug="other-slug",
        )
        return category.pk

    def __str__(self):
        return self.name


class Image(django.db.models.Model):
    image = django.db.models.ImageField(
        verbose_name="изображение",
        upload_to="catalog/",
    )
    item = django.db.models.ForeignKey(
        verbose_name="товар",
        to="Item",
        on_delete=django.db.models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return self.image.url

    def get_image_x1280(self):
        return sorl.thumbnail.get_thumbnail(self.image, "1280", quality=51)

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            thumbnail = self.get_image_300x300()
            return django.utils.safestring.mark_safe(
                f'<img src="{thumbnail.url}">',
            )

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True


class Item(core.models.AbstractModel):
    text = django_ckeditor_5.fields.CKEditor5Field(
        verbose_name="текст",
        validators=[
            catalog.validators.ValidateMustContain("роскошно", "превосходно"),
        ],
        help_text="Описание должно содержать "
        'слова "роскошно" или "превосходно"',
    )
    category = django.db.models.ForeignKey(
        verbose_name="категории",
        to=Category,
        on_delete=django.db.models.CASCADE,
        default=Category.get_default_pk,
        help_text="Выберите категорию",
        related_name="items",
    )
    tags = django.db.models.ManyToManyField(
        verbose_name="теги",
        to=Tag,
        help_text="Выберите теги",
        related_name="items",
    )
    MainImage = django.db.models.OneToOneField(
        verbose_name="главное изображение",
        to=Image,
        on_delete=django.db.models.CASCADE,
        related_name="item_main",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]
