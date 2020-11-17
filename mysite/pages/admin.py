from django.contrib import admin
from django.contrib.auth.models import User
from .models import Group, Event
# Register your models here.

admin.site.register(Group)
admin.site.register(Event)