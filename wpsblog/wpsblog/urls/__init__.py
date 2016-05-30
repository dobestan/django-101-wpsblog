from django.conf.urls import url, include
from django.contrib import admin

from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^about/us/$', about, name="about"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),

    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy")),
]
