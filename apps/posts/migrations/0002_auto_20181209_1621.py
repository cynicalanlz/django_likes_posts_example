# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-09 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('39680163-2fed-4026-adb6-98bb7afb8b83'), primary_key=True, serialize=False),
        ),
    ]
