import requests

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("<h1>hello world</h1><p>This is home page.</p>")


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
    )

