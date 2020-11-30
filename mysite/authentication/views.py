from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from .forms import CreateAccountForm, UserUpdateForm
from django.shortcuts import render



class CreateAccountView(View):

    def get(self, request, *args, **kwargs):
        form = CreateAccountForm()
        return render(request, 'form.html', {'form': form, 'title': 'Create Account'})

    def post(self, request, *args, **kwargs):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # check if user already exists
            new_user = form.save()
            return render(request, 'message.html', {'title': 'Success', 'message': f'Successfully created a new account, welcome {new_user}'})
        else:
            return render(request, 'message.html', {'title': 'Failure', 'message': 'One or more required fields had an error in it.'})

