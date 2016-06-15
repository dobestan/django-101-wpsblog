from django.test import TestCase


class PricingViewTestCase(TestCase):

    def setUp(self):
        self.response = self.client.get("/pricing/")

    def test_pricing_view_should_return_200(self):
        self.assertEqual(
            self.response.status_code,
            200,
        )

    def test_pricing_view_should_have_good_title(self):
        self.assertContains(
            self.response,
            "Pricing Table",
        )
