from django.shortcuts import render
from django.views import generic

from fashion.models import Item, Category


def index(request):
    items = Item.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "items": items,
        "num_visits": num_visits,
    }

    return render(request, "fashion/index.html", context)


class CategoryListView(generic.ListView):
    queryset = Category.objects.all()
    context_object_name = "categories_list"
    template_name = "fashion/categories.html"


class BusinessWearListView(generic.ListView):
    queryset = Item.objects.filter(categories__name="Business")
    context_object_name = "business_wear_list"
    template_name = "fashion/business.html"
