from django.contrib import admin
from django.urls import path, include

from homepage.views import home
from catalog.views import item_list, item_detail
from about.views import description


urlpatterns = [
    path("", home),
    path("about/", description),
    path("admin/", admin.site.urls),
    path("catalog/", item_list),
    path("catalog/<int:pk>/", item_detail),
]

urlpatterns += path("__debug__/", include("debug_toolbar.urls"))