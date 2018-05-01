# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from subject.models import Stream, Subject
import datetime

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=50, unique=True)
    function_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_function_name(self):
        return self.function_name

class Assignment(models.Model):
    stream_id = models.ForeignKey(Stream,
        on_delete=models.CASCADE,null=False,blank=False)
    title = models.CharField(max_length=50, unique=True)
    start_time = models.DateTimeField(default=datetime.date.today)
    end_time = models.DateTimeField(default=datetime.date.today, null=True)
    is_exam = models.BooleanField(default=False)

class AssignmentTopic(models.Model):
    assignment_id = models.ForeignKey(Assignment,
        on_delete=models.CASCADE,null=False,blank=False)
    topic_id = models.ForeignKey(Topic,
        on_delete=models.CASCADE,null=False,blank=False)
    example_amount = models.IntegerField(default=1)
    points = models.IntegerField(default=5)
