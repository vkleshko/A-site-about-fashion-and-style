from django.urls import path

from fashion.views import (
    index,
    CategoryListView,
    BusinessWearListView
)

urlpatterns = [
    path("", index, name="index"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/business/", BusinessWearListView.as_view(), name="business-wear"),

]
app_name = "fashion"
