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
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects,
        pk=pk,
        is_published=True,
    )
    return django.shortcuts.render(request, template, {"item": item})
