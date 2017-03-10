from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TeacherLogin(models.Model):
	TEACHER_ID = models.CharField(max_length=100)
	TEACHER_NAME = models.CharField(max_length=100)
	TEACHER_EMAIL = models.CharField(max_length=100)
	TEACHER_CONTACT_NUMBER = models.IntegerField()
	TEACHER_ENCRYPTED_PASSWORD = models.CharField(max_length=100)
