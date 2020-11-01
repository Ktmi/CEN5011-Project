from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Group(models.Model):
    id = models.ForeignKey(User, primary_key = True, on_delete=models.CASCADE)

class GroupMember(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(name = 'unique_Group_Member', fields = ['user_id', 'group_id'])
        ]
        indexes = [
            models.Index(fields=['group_id', 'user_id'])
        ]

class Event(models.Model):
    host_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=datetime.time.min)
    end_time = models.TimeField(default=datetime.time.max)

class Attendee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(name = 'unique_Event_Attendee', fields=['event_id', 'attendee_id'])
        ]
        indexes = [
            models.Index(fields=['event_id', 'attendee_id'])
        ]