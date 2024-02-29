import django.http
import django.shortcuts

__all__ = ["description"]


def description(request):
    template = "about/about.html"
    return django.shortcuts.render(request, template)
