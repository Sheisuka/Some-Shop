from django.contrib import admin
from django.urls import include, path

from about.views import description
from catalog.views import item_detail, item_list
from homepage.views import home


urlpatterns = [
    path("", home),
    path("about/", description),
    path("admin/", admin.site.urls),
    path("catalog/", item_list),
    path("catalog/<int:pk>/", item_detail),
]

urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)
