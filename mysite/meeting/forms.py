from django import forms
from pages.models import Event
from django import forms

class CreateMeetingForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'date', 'start_time', 'end_time', 'description', 'zip_code')


