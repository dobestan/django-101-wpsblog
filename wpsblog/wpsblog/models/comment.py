from django.db import models
from django.core.urlresolvers import reverse


class Comment(models.Model):

    post = models.ForeignKey("Post")

    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "post_id": self.post.id,
            },
        ) + "#comment-" + str(self.id)
