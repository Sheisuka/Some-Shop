import uuid

import django.core.validators
import django.db.models
import django.shortcuts
import django.utils.safestring
import django_ckeditor_5.fields
import sorl.thumbnail

import catalog.validators
import core.models

__all__ = ["Category", "ImageBaseModel", "Image", "MainImage", "Item", "Tag"]


def item_directory_path(instance, filename):
    return f"catalog/{instance.item.id}/{uuid.uuid4()}-{filename}"


class ContentManager(django.db.models.Manager):
    def on_main(self):
        main_items = (
            catalog.models.Item.objects.select_related("category", "main_image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                ),
            )
            .filter(
                is_published=True,
                is_on_main=True,
                category__is_published=True,
            )
            .only(
                "pk",
                "name",
                "text",
                "category__name",
                "tags",
                "main_image__image",
            )
            .order_by("name")
        )
        
        return main_items
    
    def published(self):
        published_items = (
            catalog.models.Item.objects.select_related("category", "main_image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                ),
            )
            .filter(is_published=True, category__is_published=True)
            .only(
                "pk",
                "name",
                "text",
                "category__name",
                "tags",
                "main_image__image",
            )
        .order_by("category__name")
        )
        
        return published_items

    def get_item(self, pk):
        tags_query = catalog.models.Tag.objects.filter(is_published=True).only(
        "name",
        )
        images_query = catalog.models.Image.objects.only("id", "image", "item_id")
        items_query = (
            catalog.models.Item.objects.select_related("category", "main_image")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=tags_query,
                ),
            )
            .prefetch_related(
                django.db.models.Prefetch(
                    "images",
                    queryset=images_query,
                ),
            )
            .filter(is_published=True, category__is_published=True)
            .only("name", "text", "category__name", "main_image__image")
        )

        item = django.shortcuts.get_object_or_404(
            items_query,
            pk=pk,
        )
    
        return item


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


class ImageBaseModel(django.db.models.Model):
    image = django.db.models.ImageField(
        verbose_name="изображение",
        upload_to=item_directory_path,
        default=None,
        null=True,
    )

    class Meta:
        abstract = True

    def get_image_x1280(self):
        return sorl.thumbnail.get_thumbnail(self.image, "1280", quality=51)

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    @property
    def get_image_50x50(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "50x50",
            crop="center",
            quality=51,
        )


class MainImage(ImageBaseModel):
    item = django.db.models.OneToOneField(
        verbose_name="Главное изображение",
        to="Item",
        on_delete=django.db.models.CASCADE,
        related_name="main_image",
        default=None,
        null=True,
    )

    def __str__(self):
        if self.item:
            return self.item.name
        return "---"

    class Meta:
        verbose_name = "главное изображение"
        verbose_name_plural = "главные изображения"


class Image(ImageBaseModel):
    item = django.db.models.ForeignKey(
        verbose_name="товар",
        to="Item",
        on_delete=django.db.models.CASCADE,
        related_name="images",
        default=None,
        null=True,
    )

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        if self.item:
            return self.item.name
        return "---"


class Item(core.models.AbstractModel):
    objects = ContentManager()

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
        related_query_name="item",
    )
    tags = django.db.models.ManyToManyField(
        verbose_name="теги",
        to=Tag,
        help_text="Выберите теги",
        related_name="items",
    )

    is_on_main = django.db.models.BooleanField(
        verbose_name="находится на главной",
        default=False,
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]

    def image_tmb(self):
        if self.main_image.image:
            return django.utils.safestring.mark_safe(
                f"<img src='{self.main_image.get_image_50x50.url}'>",
            )
        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True
