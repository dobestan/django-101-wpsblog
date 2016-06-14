from django.db import models


class BitlinkLog(models.Model):

    bitlink = models.ForeignKey("Bitlink")

    http_referer = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_user_agent = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_remote_address = models.CharField(
        max_length=31,
        blank=True,
        null=True,
    )

    http_meta_json = models.TextField(blank=True, null=True, )

    created_at = models.DateTimeField(auto_now_add=True)
