from django.urls import path

from fashion.views import (
    index,
    CategoryListView,
    BusinessWearListView,
    CasualWearListView,
    FormalWearListView
)

urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/business/", BusinessWearListView.as_view(), name="business-wear"),
    path("categories/casual/", CasualWearListView.as_view(), name="casual-wear"),
    path("categories/formal/", FormalWearListView.as_view(), name="formal-wear"),
]
app_name = "fashion"
