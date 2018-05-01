# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0003_auto_20180421_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('start_time', models.DateTimeField(default=datetime.date.today)),
                ('end_time', models.DateTimeField(default=datetime.date.today, null=True)),
                ('is_exam', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('example_amount', models.IntegerField(default=1)),
                ('points', models.IntegerField(default=5)),
                ('assignment_id', models.ForeignKey(to='subject.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('enroll_key', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('function_name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='code',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='enroll_key',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='users',
        ),
        migrations.AddField(
            model_name='topic',
            name='subject_id',
            field=models.ForeignKey(to='subject.Subject'),
        ),
        migrations.AddField(
            model_name='stream',
            name='subject_id',
            field=models.ForeignKey(to='subject.Subject'),
        ),
        migrations.AddField(
            model_name='stream',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='assignmenttopic',
            name='topic_id',
            field=models.ForeignKey(to='subject.Topic'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='stream_id',
            field=models.ForeignKey(to='subject.Stream'),
        ),
    ]
