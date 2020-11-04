from django.contrib import admin
from django.contrib.auth.models import User
from .models import Group, GroupMember, Event, Attendee
# Register your models here.

# admin.site.register(User)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Event)
admin.site.register(Attendee)