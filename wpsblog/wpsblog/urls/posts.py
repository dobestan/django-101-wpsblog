from django.conf.urls import url

from wpsblog.views.posts import *


urlpatterns = [
    url(r'^$', list, name="list"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<post_id>\d+)/$', detail, name="detail"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),

    # Comments
    url(r'^(?P<post_id>\d+)/comments/create/$', comments_create, name="comments-create"),
]
