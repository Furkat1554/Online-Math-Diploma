# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_subject_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
