from django.conf.urls import url
from django.contrib import admin

from django.http.response import HttpResponse


def home(request):
    return HttpResponse("hello world")


def room(request, room_id):
    return HttpResponse("This is a room detail " + room_id)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home),
    url(r'^rooms/(?P<room_id>\d+)/$', room),
]
