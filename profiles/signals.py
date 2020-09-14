from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile
from licenses.models import License

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(User=instance)
    
    instance.UserProfile.save()

@receiver(post_save, sender=License)
def add_license(sender, instance, **kwargs):
    instance.UserProfile.save()
