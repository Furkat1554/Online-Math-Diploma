# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-27 17:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0012_auto_20180430_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('start_time', models.DateTimeField(default=datetime.date.today)),
                ('end_time', models.DateTimeField(default=datetime.date.today, null=True)),
                ('is_exam', models.BooleanField(default=False)),
                ('stream_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Stream')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example_amount', models.IntegerField(default=1)),
                ('points', models.IntegerField(default=5)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('function_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_name',
            new_name='subject_code',
        ),
        migrations.AddField(
            model_name='assignmenttopic',
            name='topic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Topic'),
        ),
    ]
