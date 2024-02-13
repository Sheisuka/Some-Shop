from django.contrib import admin
from django.urls import include, path, re_path

from about.views import description
from catalog.views import item_detail, item_list, re_view
from homepage.views import coffee, home


urlpatterns = [
    path("", home),
    path("about/", description),
    path("admin/", admin.site.urls),
    path("catalog/", item_list),
    path("catalog/<int:pk>/", item_detail),
    re_path(r"^catalog\/re\/[1-9][0-9]*\/$", re_view),
    path("coffee/", coffee)
]

urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
