from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateAccountForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')
