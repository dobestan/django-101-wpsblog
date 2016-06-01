from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post-detail",
            kwargs={
                "post_id": self.id,
            }
        )


class NaverPost(models.Model):

    keyword = models.CharField(
        max_length=16,
    )
    title = models.CharField(
        max_length=256,
    )
    content = models.TextField()
    thumbnail_image_url = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return self.title
