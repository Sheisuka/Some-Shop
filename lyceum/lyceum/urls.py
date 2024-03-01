import django.conf
import django.conf.urls.static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("", include("homepage.urls")),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
) + [
    path(
        "ckeditor5/",
        include("django_ckeditor_5.urls"),
        name="ck_editor_5_upload_file",
    ),
]


if django.conf.settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
