# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180419_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilegroup',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
