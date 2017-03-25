from django.db import models
from login.models import SchoolUser

class Teacher(models.Model):
	username = models.CharField(max_length=200, primary_key=True)
	password = models.CharField(max_length=50)
	accessToken = models.CharField(max_length=20)
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=200) #primary, secondary, senior
	email = models.CharField(max_length=200)
	age = models.IntegerField(null=True, blank=True)
	contactNum = models.CharField(max_length=12, null=True, blank=True)
	areaOfExpertise = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	preferredLocation = models.CharField(max_length=50, null=True, blank=True)
	qualification = models.CharField(max_length=100, null=True, blank=True)
	teachingExperience = models.IntegerField(null=True, blank=True)
	currentSchool = models.ForeignKey(
        SchoolUser,
        on_delete=models.CASCADE,
		null=True,
		blank=True,
    )

class Attendance_Present(models.Model):
	teacher_username = models.ForeignKey(
	        'Teacher',
	        on_delete=models.CASCADE,
	    )
	date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	latitude_1 = models.FloatField(null=True, blank=True)
	longitude_1 = models.FloatField(null=True, blank=True)
	latitude_2 = models.FloatField(null=True, blank=True)
	longitude_2 = models.FloatField(null=True, blank=True)
	latitude_3 = models.FloatField(null=True, blank=True)
	longitude_3 = models.FloatField(null=True, blank=True)
	latitude_4 = models.FloatField(null=True, blank=True)
	longitude_4 = models.FloatField(null=True, blank=True)
	accuracy = models.FloatField(null=True, blank=True)

class Attendance_Holiday(models.Model):
	school_user = models.ForeignKey(
	        SchoolUser,
	        on_delete=models.CASCADE,
	    )
	date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
