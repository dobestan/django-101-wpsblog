from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from wpsblog.models import Post


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect(
        reverse("post-list"),
    )
