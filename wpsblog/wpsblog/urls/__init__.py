from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from wpsblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/us/$', about, name="about"),
    url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
    url(r'^news/$', news, name="news"),

    url(r'^policy/', include("wpsblog.urls.policy", namespace="policy")),
    url(r'^posts/', include("wpsblog.urls.posts", namespace="posts")),
    url(r'^', include("wpsblog.urls.auth", namespace="auth")),

    url(r'^naver/posts/$', naver_posts_list, name="naver-posts-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
