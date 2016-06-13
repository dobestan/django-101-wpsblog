from django.shortcuts import redirect, render

from wpsblog.models import Post, Comment


def comments_create(request, post_id):
    content = request.POST.get("content")
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.create(
        user=request.user,
        content=content,
    )
    return redirect(comment)


def comments_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    return render(
        request,
        "posts/comments_edit.html",
        {
            "post": post,
            "comment": comment,
        },
    )


def comments_update(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    content = request.POST.get("content")
    comment.content = content
    comment.save()

    return redirect(comment)


def comments_delete(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.delete()
    return redirect(post)
