from django import forms

class CreateAccountForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 16, min_length = 6,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label = 'Email',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label = 'First name',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label = 'Last name',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Password', max_length = 16, min_length = 6,
                               widget = forms.PasswordInput(attrs={'class': 'form-control'}))
