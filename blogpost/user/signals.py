import django.db.models.signals as signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(signals.post_save, sender=User)
def build_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()