from django.shortcuts import redirect
from django.views.generic import View

from bitly.models.bitlink import Bitlink


class BitlinkRedirectView(View):

    def get(self, request, *args, **kwargs):

        bitlink = Bitlink.objects.get(
            shorten_hash=kwargs.get("shorten_hash"),
        )

        return redirect(bitlink.original_url)
