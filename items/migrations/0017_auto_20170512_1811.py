# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-12 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_auto_20170511_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='btype',
        ),
        migrations.RemoveField(
            model_name='item',
            name='teleport',
        ),
    ]
