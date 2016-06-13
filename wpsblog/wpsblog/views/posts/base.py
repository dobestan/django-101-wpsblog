from django.views.generic import View

from wpsblog.models import Post


class PostBaseView(View):
    model = Post
