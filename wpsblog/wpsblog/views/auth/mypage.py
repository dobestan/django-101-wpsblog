from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "auth/mypage.html"
