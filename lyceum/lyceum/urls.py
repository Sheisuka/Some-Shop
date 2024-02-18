from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("", include("homepage.urls"))
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
