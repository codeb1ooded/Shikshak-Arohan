# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-19 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170319_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooluser',
            name='id',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='wifi_zone',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='schooluser', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
