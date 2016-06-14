from django.views.generic import View
from django.views.generic.edit import CreateView

from django.shortcuts import redirect, render

from wpsblog.models import Post, Comment


class CommentBaseView(View):
    model = Comment


class PostCommentCreateView(CommentBaseView, CreateView):
    fields = [
        "content",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
            id=self.kwargs.get("post_id"),
        )

        return super(PostCommentCreateView, self).form_valid(form)


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
