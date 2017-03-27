from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class SchoolUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="schooluser")
    name = models.CharField(max_length=50)
    timing = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    state_id = models.CharField(max_length=3, blank=True)
    district = models.CharField(max_length=30, blank=True)
    district_id = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=30, blank=True)
    city_id = models.CharField(max_length=9, blank=True)
    numOfStudents = models.IntegerField(blank=True, default=100)
    numOfTeachers = models.IntegerField(blank=True, default=10)
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

    def __str__(self):
        return "Id: "+ self.id + " Name: " + self.state_name


class District(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    district_name = models.CharField(max_length=50, blank=True)
    headquaters = models.CharField(max_length=50, blank=True)
    state_foreign_id = models.CharField(max_length=3, blank=True)


    def __str__(self):
        return "Id: "+ self.id + " Name: " + self.district_name +" Foreign Key: "+ self.state_foreign_id

class City(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    city_name = models.CharField(max_length=50, blank=True)
    city_ids = models.CharField(max_length=50, blank=True)
    district_foreign_id = models.CharField(max_length=6, blank=True)


    def __str__(self):
        return "Id: "+ self.id + " Name: " + self.city_name +" Foreign Key: "+ self.district_foreign_id
