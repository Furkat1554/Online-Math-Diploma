# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20180420_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='user',
            new_name='users',
        ),
    ]
