from django.db import models


class Comment(models.Model):

    post = models.ForeignKey("Post")

    content = models.TextField()

    def __str__(self):
        return self.content
