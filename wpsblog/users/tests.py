from django.test import TestCase

from django.contrib.auth.models import User


class UserProfileModelTestCase(TestCase):

    def test_user_should_have_user_profile(self):
        test_username = "test_username"
        test_password = "test_password"

        user = User.objects.create_user(
            username=test_username,
            password=test_password,
        )

        self.assertTrue(
            user.userprofile,
        )
