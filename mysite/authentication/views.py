from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from .forms import CreateAccountForm
from django.shortcuts import render



class CreateAccountView(View):

    return_address = '/'

    def get(self, request, *args, **kwargs):
        form = CreateAccountForm()
        return render(request, 'form.html', {'form': form, 'title': 'Create Account', 'return_address': self.return_address})

    def post(self, request, *args, **kwargs):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # check if user already exists

            new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
