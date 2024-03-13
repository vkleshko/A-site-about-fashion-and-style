from django.shortcuts import render

from fashion.models import Item


def index(request):
    items = Item.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "items": items,
        "num_visits": num_visits,
    }

    return render(request, "fashion/index.html", context)
