from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth import get_user_model
import os

@receiver(pre_save, sender=Profile, dispatch_uid="supprimer_ancienne_image")
def supprimer_ancienne_image(sender, instance, **kwargs):
    print("supprimer_ancienne_image")
    if instance.pk:
        ancien_profile = Profile.objects.get(pk=instance.pk)
        if ancien_profile.profile_pic and ancien_profile.profile_pic != instance.profile_pic:
            old_avatar_path = ancien_profile.profile_pic.path
            if os.path.isfile(old_avatar_path):
                os.remove(old_avatar_path)
