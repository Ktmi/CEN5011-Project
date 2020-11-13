from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from .forms import CreateAccountForm
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
