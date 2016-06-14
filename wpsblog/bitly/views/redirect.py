from django.shortcuts import redirect
from django.views.generic import View

from bitly.models.bitlink import Bitlink


class BitlinkRedirectView(View):

    def get(self, request, *args, **kwargs):

        bitlink = Bitlink.objects.get(
            shorten_hash=kwargs.get("shorten_hash"),
        )

        bitlink_log = bitlink.bitlinklog_set.create(
            http_referer=request.META.get("HTTP_REFERER"),
            http_user_agent=request.META.get("HTTP_USER_AGENT"),
            http_remote_address=request.META.get("REMOTE_ADDR"),
            http_meta_json=str(request.META),
        )

        return redirect(bitlink.original_url)
