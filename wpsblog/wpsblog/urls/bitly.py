from django.conf.urls import url

from bitly.views import *


urlpatterns = [
    url(r'new/$', BitlinkCreateView.as_view(), name="create"),
]
