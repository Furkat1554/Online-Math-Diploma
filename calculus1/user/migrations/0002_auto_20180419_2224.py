# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('enroll_key', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='profilegroup',
            name='code',
        ),
        migrations.RemoveField(
            model_name='profilegroup',
            name='enroll_key',
        ),
    ]
