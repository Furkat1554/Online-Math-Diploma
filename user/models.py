from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class ProfileGroup(models.Model):
    title = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    student_group = models.ForeignKey(ProfileGroup, on_delete=models.CASCADE,null=True,blank=True)
    student_grade = models.IntegerField(default=1)

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def grade_update(self, value):
        self.user_grade = Decimal(value)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
