from django.conf.urls import url

from bitly.views import *


urlpatterns = [
    url(r'new/$', BitlinkCreateView.as_view(), name="create"),
    url(r'(?P<shorten_hash>\w+)/dashboard/$', BitlinkDashboardView.as_view(), name="dashboard"),
    url(r'(?P<shorten_hash>\w+)/$', BitlinkRedirectView.as_view(), name="redirect"),
]
