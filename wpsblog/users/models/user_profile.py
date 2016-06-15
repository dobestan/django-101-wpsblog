from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    is_phonenumber_exist = models.BooleanField(
        default=False,
    )
    is_signup_sms_sent = models.BooleanField(
        default=False,
    )
