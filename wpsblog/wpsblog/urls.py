from django.conf.urls import url
from django.contrib import admin

from wpsblog.views import home, room


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home),
    url(r'^rooms/(?P<room_id>\d+)/$', room),
]
