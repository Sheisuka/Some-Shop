from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PositiveIntegerConverter, "pint")

urlpatterns = [
    path("", views.item_list),
    path("<int:pk>/", views.item_detail),
    re_path(r"^re\/(?P<value>[1-9][0-9]*)\/?$", views.re_view),
    path("converter/<pint:value>/", views.converter_view),
]
