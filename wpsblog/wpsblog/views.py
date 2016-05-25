import json
import requests

from django.http.response import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(
        template.render(
            {"site_name": "wps blog"},
            request,
        )
    )


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
    )


def news(request):
    search = request.GET.get("search")

    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
    news_dict = json.loads(response.text)
    news_list = news_dict.get("news")

    if search:
        news_list = list(filter(
            lambda news: search in news.get('title'),
            news_list,
        ))

    count = len(news_list)
    news_content = "".join([
        "<h2>{title}</h2><img src={image_src}><p>{content}</p>".format(
            title=news.get('title'),
            image_src=news.get('image'),
            content=news.get('content'),
        )
        for news
        in news_list
    ])
