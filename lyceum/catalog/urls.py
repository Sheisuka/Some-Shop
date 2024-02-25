import django.urls

import catalog.converters
import catalog.views

django.urls.register_converter(
    catalog.converters.PositiveIntegerConverter, "pint"
)

urlpatterns = [
    django.urls.path("", catalog.views.item_list),
    django.urls.path("<int:pk>/", catalog.views.item_detail),
    django.urls.re_path(
        r"^re\/(?P<pk>[1-9][0-9]*)\/?$",
        catalog.views.item_detail,
    ),
    django.urls.path("converter/<pint:pk>/", catalog.views.item_detail),
]
