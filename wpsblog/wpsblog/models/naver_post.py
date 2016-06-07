from django.db import models


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
