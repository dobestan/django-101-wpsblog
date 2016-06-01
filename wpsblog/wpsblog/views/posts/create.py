from django.shortcuts import redirect

from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    post = Post.objects.create(
        title=title,
        content=content,
    )

    return redirect(post)
