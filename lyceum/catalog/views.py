import django.db.models
import django.http
import django.shortcuts

import catalog.models

__all__ = ["item_detail", "item_list"]


def item_list(request):
    template = "catalog/item_list.html"

    items = (
        catalog.models.Item.objects.select_related("category", "main_image")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True,
                ).only("name"),
            ),
        )
        .filter(is_published=True)
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
    return django.shortcuts.render(request, template, {"items": items})


def item_detail(request, pk):
    template = "catalog/item.html"

    tags_query = catalog.models.Tag.objects.filter(is_published=True).only(
        "name",
    )
    images_query = catalog.models.Image.objects.only("id", "image", "item_id")
    items_query = (
        catalog.models.Item.objects.filter(is_published=True)
        .select_related("category", "main_image")
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
        .only("name", "text", "category__name", "main_image__image")
    )

    item = django.shortcuts.get_object_or_404(
        items_query,
        pk=pk,
    )

    return django.shortcuts.render(request, template, {"item": item})
