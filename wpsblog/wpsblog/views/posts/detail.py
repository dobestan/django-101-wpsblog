from django.views.generic.detail import DetailView

from wpsblog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
