from django.contrib import admin
from django.urls import include, path

from homepage.views import coffee, home


urlpatterns = [
    path("", home),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("coffee/", coffee)
]

urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
