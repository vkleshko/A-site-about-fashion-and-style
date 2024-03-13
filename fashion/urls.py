from django.urls import path

from fashion.views import index

urlpatterns = [
    path("", index, name="index"),

]
app_name = "fashion"
