import http

import django.db.models
import django.http
import django.shortcuts

import catalog.models

__all__ = ["coffee", "home"]


def home(request):
    template = "homepage/main.html"
    main_items = catalog.models.Item.objects.on_main()
    return django.shortcuts.render(request, template, {"items": main_items})


def coffee(request):
    return django.http.HttpResponse(
        "Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
