import django.conf
import django.conf.urls.static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("homepage.urls")),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

if django.conf.settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
