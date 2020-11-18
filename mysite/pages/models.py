from django.db import models
from django.contrib.auth.models import User
import datetime

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
