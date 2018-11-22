# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0016_stream_stream_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentdone',
            name='assignment_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='subject.Assignment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignmentdone',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignmentdone',
            name='topic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.AssignmentTopic'),
        ),
    ]