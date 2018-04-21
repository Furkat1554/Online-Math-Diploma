from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)
    enroll_key = models.CharField(max_length=10)
    users = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title
