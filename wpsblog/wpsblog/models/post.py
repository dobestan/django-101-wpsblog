from django.db import models
from django.core.urlresolvers import reverse


class PostManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()

    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "posts:detail",
            kwargs={
                "post_id": self.id,
            }
        )

    def get_update_url(self):
        return reverse(
            "posts:update",
            kwargs={
                "post_id": self.id,
            }
        )
