from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class SchoolUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="schooluser")
    timing = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    wifi_zone = models.NullBooleanField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=SchoolUser)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()
