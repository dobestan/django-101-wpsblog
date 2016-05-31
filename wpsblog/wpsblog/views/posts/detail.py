from django.shortcuts import render

from wpsblog.models import Post


def detail(request, post_id):
    return render(
        request,
        "posts/detail.html",
        {
            "post": Post.objects.get(id=post_id),
        },
    )
