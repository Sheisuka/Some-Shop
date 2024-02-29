import django.urls

import catalog.converters
import catalog.views

django.urls.register_converter(
    catalog.converters.PositiveIntegerConverter,
    "pint",
)

app_name = "catalog"

urlpatterns = [
    django.urls.path("", catalog.views.item_list, name="item_list"),
    django.urls.path(
        "<int:pk>/", catalog.views.item_detail, name="item_detail",
    ),
    django.urls.re_path(
        r"^re\/(?P<pk>[1-9][0-9]*)\/?$",
        catalog.views.item_detail,
        name="re_item_detail",
    ),
    django.urls.path("converter/<pint:pk>/", catalog.views.item_detail, name="converter_item_detail"),
]
