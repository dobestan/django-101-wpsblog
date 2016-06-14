from django.conf.urls import url

from bitly.views import *


urlpatterns = [
    url(r'(?P<shorten_hash>\w+)/$', BitlinkRedirectView.as_view(), name="redirect"),
    url(r'new/$', BitlinkCreateView.as_view(), name="create"),
]
