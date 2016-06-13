from django.conf.urls import url

from wpsblog.views.auth import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^my/page/$', mypage, name="mypage"),
]
