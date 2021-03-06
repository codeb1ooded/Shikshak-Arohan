from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

def random_num():
    return random.randint(100, 500)

class SchoolUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="schooluser")
    name = models.CharField(max_length=50)
    timing = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    state_id = models.CharField(max_length=3, blank=True)
    state_instance = models.ForeignKey(
	        'State',
	        on_delete=models.CASCADE,
            blank=True,
            null=True
	    )
    district = models.CharField(max_length=30, blank=True)
    district_id = models.CharField(max_length=6, blank=True)
    district_instance = models.ForeignKey(
	        'District',
	        on_delete=models.CASCADE,
            blank=True,
            null=True
	    )
    city = models.CharField(max_length=30, blank=True)
    city_id = models.CharField(max_length=9, blank=True)
    city_instance = models.ForeignKey(
	        'City',
	        on_delete=models.CASCADE,
            blank=True,
            null=True
	    )
    numOfStudentsPrimary = models.IntegerField(default=random_num())
    numOfStudentsSecondary = models.IntegerField(default=random_num())
    numOfStudentsSenior = models.IntegerField(default=random_num())
    numOfTeachersPrimary = models.IntegerField(default=10)
    numOfTeachersSecondary = models.IntegerField(default=10)
    numOfTeachersSenior = models.IntegerField(default=10)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    wifi_zone = models.BooleanField(default=False)

    def __str__(self):
        return "Username:" + self.user.username + "  Name:" + self.name

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

    def getName(self):
        return self.state_name


class District(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    district_name = models.CharField(max_length=50, blank=True)
    headquaters = models.CharField(max_length=50, blank=True)
    state_foreign_id = models.ForeignKey(
	        'State',
	        on_delete=models.CASCADE,
            blank=True,
            null=True
	    )

    def __str__(self):
        return "Id: " + self.id + " Name:" + self.district_name + " Foreign key:" + self.state_foreign_id.id

    def getName(self):
        return self.district_name

class City(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    city_name = models.CharField(max_length=50, blank=True)
    city_ids = models.CharField(max_length=50, blank=True)
    district_foreign_id = models.ForeignKey(
	        'District',
	        on_delete=models.CASCADE,
            blank=True,
            null=True
	    )

    def __str__(self):
        return "Id: "+ self.id + " Name: " + self.city_name +" Foreign Key: "+ self.district_foreign_id.id

    def getName(self):
        return self.city_name


class ThresholdValues(models.Model):
    category_name = models.CharField(max_length = 255, blank = False, null = False)
    min_val = models.FloatField(blank = False, null = False)
    max_val = models.FloatField(blank = False, null = False)
    color_code = models.CharField(max_length = 10, blank = False, null = False)
