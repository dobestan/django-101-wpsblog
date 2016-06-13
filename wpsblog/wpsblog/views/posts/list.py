from django.views.generic.list import ListView
from django.core.paginator import Paginator

from wpsblog.models import Post

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_paginate_by(self, queryset):
        return self.request.GET.get("per", 5)
