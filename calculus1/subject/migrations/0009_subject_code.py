# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_remove_subject_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]