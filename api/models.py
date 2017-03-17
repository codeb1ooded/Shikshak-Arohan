from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=200,primary_key=True)
	password = models.CharField(max_length=50)
	auth12 = models.CharField(max_length=20)
	name = models.CharField(max_length=200)

class Resume(models.Model):
	username = models.CharField(max_length=200,primary_key=True)
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	contactNum = models.CharField(max_length=12)
	email = models.CharField(max_length=100)
	areaOfExpertise = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	prefferedLocation = models.CharField(max_length=50)
	qualification = models.CharField(max_length=100)
	teachingExperience = models.IntegerField()
	currentSchool = models.CharField(max_length=100)

class Teacher(models.Model):
	username = models.CharField(max_length=200, primary_key=True)
	password = models.CharField(max_length=50)
	auth12 = models.CharField(max_length=20)
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	contactNum = models.CharField(max_length=12)
	email = models.CharField(max_length=100)
	areaOfExpertise = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	preferredLocation = models.CharField(max_length=50)
	qualification = models.CharField(max_length=100)
	teachingExperience = models.IntegerField()
	currentSchool = models.CharField(max_length=100)   # would be a foreign key

class Attendance(models.Model):
	teacher_username = models.ForeignKey(
	        'Teacher',
	        on_delete=models.CASCADE,
	    )
	date = models.DateField(auto_now=False, auto_now_add=False)
	presence = models.IntegerField()
