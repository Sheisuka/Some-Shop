import http

import django.http
import django.shortcuts


def home(request):
    template = "homepage/main.html"

    return django.shortcuts.render(request, template)


def coffee(request):
    response = django.http.HttpResponse(
        "Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
    return response
