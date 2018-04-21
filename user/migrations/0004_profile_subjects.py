# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180419_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subjects',
            field=models.ManyToManyField(to='user.Subject'),
        ),
    ]
