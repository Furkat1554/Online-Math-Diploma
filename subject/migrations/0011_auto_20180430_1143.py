# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0010_remove_subject_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='stream_id',
        ),
        migrations.RemoveField(
            model_name='assignmenttopic',
            name='assignment_id',
        ),
        migrations.RemoveField(
            model_name='assignmenttopic',
            name='topic_id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='subject_id',
        ),
        migrations.AddField(
            model_name='subject',
            name='project_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='AssignmentTopic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
