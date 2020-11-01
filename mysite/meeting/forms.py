from django import forms

class CreateMeetingForm(forms.Form):
    name = forms.CharField(label = 'Event Name', max_length = 64, min_length = 8,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label = 'Day of Event',
                           widget=forms.DateInput(attrs={'class': 'form-control'}))
    start_time = forms.TimeField(label = 'Start Time',
                                 widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end_time = forms.TimeField(label = 'End Time',
                               widget=forms.TimeInput(attrs={'class': 'form-control'}))