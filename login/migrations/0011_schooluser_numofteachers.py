# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-25 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20170324_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooluser',
            name='numOfTeachers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
