from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models.user_profile import UserProfile

from wpsblog.utils.sms import send_sms


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
            user=instance,
        )


@receiver(post_save, sender=UserProfile)
def post_save_userprofile(sender, instance, created, **kwargs):
    if instance.is_phonenumber_exist and not instance.is_signup_sms_sent:
        send_sms(
            instance.phonenumber,
            instance.phonenumber,
            "{username} 님의 회원가입을 축하드립니다.".format(username=instance.user.username),
        )
        instance.is_signup_sms_sent = True
        instance.save()
