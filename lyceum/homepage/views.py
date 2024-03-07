import http

import django.db.models
import django.http
import django.shortcuts

import catalog.models

__all__ = ["coffee", "home"]


def home(request):
    template = "homepage/main.html"
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
    return django.shortcuts.render(request, template, {"items": main_items})


def coffee(request):
    return django.http.HttpResponse(
        "Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
