import django.db.models
import django.http
import django.shortcuts

import catalog.models

__all__ = ["item_detail", "item_list"]


def item_list(request):
    template = "catalog/item_list.html"

    categories = (
        catalog.models.Category.objects.filter(
            is_published=True,
        )
        .only("name")
        .order_by("name")
    )

    item_query = catalog.models.Item.objects.filter(is_published=True).only(
        "name",
        "text",
        "tags",
        "main_image",
        "category",
    )
    tag_query = catalog.models.Tag.objects.filter(is_published=True).only(
        "name",
    )

    categories = categories.prefetch_related(
        django.db.models.Prefetch("items", queryset=item_query),
        django.db.models.Prefetch("items__tags", queryset=tag_query),
        "items__main_image",
    )
    return django.shortcuts.render(
        request,
        template,
        {"categories": categories},
    )


def item_detail(request, pk):
    template = "catalog/item.html"
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects,
        pk=pk,
        is_published=True,
    )
    return django.shortcuts.render(request, template, {"item": item})
