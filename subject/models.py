from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subject_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.title

class Stream(models.Model):
    users = models.ManyToManyField(User,blank=True)
    subject_id = models.ForeignKey(Subject,
        on_delete=models.CASCADE,null=False,blank=False)
    title = models.CharField(max_length=50, unique=True)
    enroll_key = models.CharField(max_length=20)

    def __str__(self):
        return self.title
