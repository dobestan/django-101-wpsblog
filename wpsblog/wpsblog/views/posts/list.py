from django.views.generic.list import ListView

from wpsblog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
