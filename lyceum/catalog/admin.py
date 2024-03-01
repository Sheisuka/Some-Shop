import django.contrib

import catalog.models

__all__ = ["ImageAdmin", "ImageInline", "ItemAdmin"]


class ImageInline(django.contrib.admin.TabularInline):
    model = catalog.models.Image
    readonly_fields = ("image_tmb",)
    extra = 0


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        "get_main_image",
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    fields = (
        "name",
        "is_published",
        "text",
        "category",
        "tags",
        "MainImage",
        "get_main_image",
    )
    readonly_fields = ("get_main_image",)
    filter_horizontal = ("tags",)
    inlines = [ImageInline]

    def get_main_image(self, obj):
        return obj.MainImage.image_tmb()

    get_main_image.short_description = "превью"


@django.contrib.admin.register(catalog.models.Image)
class ImageAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        "image_tmb",
        "image",
    )
    readonly_fields = ("image_tmb",)


django.contrib.admin.site.register(catalog.models.Category)
django.contrib.admin.site.register(catalog.models.Tag)
