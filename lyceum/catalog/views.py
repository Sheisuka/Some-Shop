import django.db.models
import django.http
import django.shortcuts

import catalog.models

__all__ = ["item_detail", "item_list"]


def item_list(request):
    template = "catalog/item_list.html"
    items = catalog.models.Item.objects.published()

    return django.shortcuts.render(request, template, {"items": items})


def item_detail(request, pk):
    template = "catalog/item.html"
    item = catalog.models.Item.objects.get_item(pk)

    return django.shortcuts.render(request, template, {"item": item})
