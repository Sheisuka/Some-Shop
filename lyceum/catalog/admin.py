import django.contrib

import catalog.models

__all__ = ["MainImageInline", "ImageInline", "ItemAdmin"]


django.contrib.admin.site.register(catalog.models.Category)
django.contrib.admin.site.register(catalog.models.Tag)
django.contrib.admin.site.register(catalog.models.MainImage)
django.contrib.admin.site.register(catalog.models.Image)


class MainImageInline(django.contrib.admin.TabularInline):
    model = catalog.models.MainImage
    fields = ("image",)


class ImageInline(django.contrib.admin.TabularInline):
    model = catalog.models.Image
    fields = ("image",)


@django.contrib.admin.register(catalog.models.Item)
class ItemAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.image_tmb,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    readonly_fields = (catalog.models.Item.image_tmb,)
    filter_horizontal = ("tags",)
    inlines = [MainImageInline, ImageInline]
