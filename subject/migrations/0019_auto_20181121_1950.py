# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-21 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0018_auto_20181027_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentdone',
            old_name='topic_id',
            new_name='assignment_topic_id',
        ),
    ]
