from django.views.generic import View
from django.http.response import HttpResponse


class PricingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Pricing Table")
