from django import forms
from pages.models import Event

class CreateMeetingForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'date', 'start_time', 'end_time', 'description')