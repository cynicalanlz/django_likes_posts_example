# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-09 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20181209_1626'),
        ('likes', '0002_auto_20181209_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.UUIDField(default=uuid.UUID('43072476-6731-4666-86cb-cb09c2a3a167'), primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'post')]),
        ),
    ]
