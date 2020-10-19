from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    id = models.ForeignKey(User, primary_key = True)

class GroupMember(models.Model):
    user_id = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['user_id', 'group_id'])
        ]

class Event(models.Model):
    host_id = models.ForeignKey(User)
    name = models.CharField(max_length=64)

class Attendee(models.Model):
    event_id = models.ForeignKey(Event)
    attendee_id = models.ForeignKey(User)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event_id', 'attendee_id'])
        ]
        indexes = [
            models.Index(fields=['event_id', 'attendee_id'])
        ]