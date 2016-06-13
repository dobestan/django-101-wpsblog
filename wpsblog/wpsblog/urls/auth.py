from django.conf.urls import url

from wpsblog.views.auth import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^my/page/$', mypage, name="mypage"),
]
