from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subject_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Stream(models.Model):
    users = models.ManyToManyField(User, blank=True)
    subject_id = models.ForeignKey(Subject,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   blank=False)
    title = models.CharField(max_length=50, unique=True)
    stream_code = models.CharField(max_length=50,
                                   unique=True)
    enroll_key = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subject_id = models.ForeignKey(Subject,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=False)
    function_code = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title

    def get_function_name(self):
        return self.function_code


class Assignment(models.Model):
    stream_id = models.ForeignKey(Stream,
                                  on_delete=models.CASCADE,
                                  null=False,
                                  blank=False)
    title = models.CharField(max_length=50, unique=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now, null=True)
    is_exam = models.BooleanField(default=False)

    def __str__(self):
        return self.stream_id.title + ': ' + self.title


class AssignmentTopic(models.Model):
    assignment_id = models.ForeignKey(Assignment,
                                      on_delete=models.CASCADE,
                                      null=False,
                                      blank=False)
    topic_id = models.ForeignKey(Topic,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 blank=False)
    example_amount = models.IntegerField(default=1)
    points = models.IntegerField(default=5)

    def __str__(self):
        return self.assignment_id.title + ': ' + self.topic_id.title


class AssignmentDone(models.Model):
    assignment_id = models.ForeignKey(Assignment,
                                      on_delete=models.CASCADE,
                                      null=False,
                                      blank=False)
    assignment_topic_id = models.ForeignKey(AssignmentTopic,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 blank=False)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False)
    count = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)
