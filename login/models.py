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
    state = models.CharField(max_length=30, blank=True)
    state_id = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=30, blank=True)
    city_id = models.CharField(max_length=10, blank=True)
    numOfStudents = models.IntegerField(null=True, blank=True)
    numOfTeachers = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    wifi_zone = models.NullBooleanField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SchoolUser.objects.create(user=instance)

@receiver(post_save, sender=SchoolUser)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()


class State(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    state_name = models.CharField(max_length=50, blank=True)
    state_ids = models.CharField(max_length=50, blank=True)

class City(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    city_name = models.CharField(max_length=50, blank=True)
    city_ids = models.CharField(max_length=50, blank=True)
    state_foreign_id = models.CharField(max_length=3, blank=True)
