from django import forms
from django.contrib.auth.models import User
from pages.models import Profile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio')