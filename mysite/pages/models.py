from django.db import models
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    members = models.ManyToManyField(User, related_name='joined_groups')

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_events')
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256, default='')
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=datetime.time.min)
    end_time = models.TimeField(default=datetime.time.max)
    attendees = models.ManyToManyField(User, related_name='joined_events')
    zip_code = models.CharField(max_length=5, default='00000')

@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_profile_for_user")
def create_profile_for_user(sender,instance=None,created=False,**kwargs):
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=64, default="###-###-####")
    profession = models.CharField(max_length=64, default="Let us know!")
    #image needs dependency
    #image = models.ImageField(default='',)

    def __str__(self):
        return f'{self.user.username} Profile'
