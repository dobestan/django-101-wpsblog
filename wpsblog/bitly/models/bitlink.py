from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save

from hashids import Hashids


class Bitlink(models.Model):

    user = models.ForeignKey(User)

    original_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return reverse(
            "bitly:redirect",
            kwargs={
                "shorten_hash": self.shorten_hash,
            }
        )


def post_save_bitlink(sender, instance, created, **kwargs):
    if created:
        hashids = Hashids(salt="awesome bitlink", min_length=4)
        instance.shorten_hash = hashids.encode(instance.id)
        instance.save()

post_save.connect(post_save_bitlink, sender=Bitlink)
