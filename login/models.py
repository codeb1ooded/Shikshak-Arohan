from __future__ import unicode_literals

from django.db import models
import datetime


class User(models.Model):
    username = models.CharField(max_length=50)
    #password = modelsforms.CharField(widget=forms.PasswordInput)
    create_time = models.DateTimeField('date created')
    phonenumber = models.IntegerField()





class Meta:
    db_table = "ShikshakArohan"
# Create your models here.
