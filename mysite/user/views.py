from pages.models import Profile
from django.contrib.auth.models import User
from django.views import View
from .forms import CreateProfileForm
from django.shortcuts import render, redirect

class ProfileView(View):
    def get(self, request, user_id, *args, **kwargs):
        user = User.objects.get(pk=user_id)
        if user is None:
            return render(request,'message.html', {'title':'User Does Not Exist','message':'No user exists with a matching id'})
        elif user.profile is None:
            return render(request,'message.html', {'title':'No profile present','message':'User has yet to create their profile'})
        else:
            return render(request, 'profile.html', {'user': user})

class MyProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile is None:
                return render(request, 'message.html', {'title':'No Profile', 'message':'You haven\'t created your proifle yet.'})
            else:
                return render(request, 'profile.html', {'user': user})
        else:
            return render(request, 'message.html', {'title': 'Not Authenticated', 'message': 'You are not currently logged in.'})

class CreateProfileView(View):
    def get(self, request, *args, **kwargs):
        form = CreateProfileForm()
        return render(request, 'form.html', {'form': form, 'title': 'Create Profile'})

    def post(self, request, *args, **kwargs):
        form = CreateProfileForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            profile = Profile(user = request.user, **form.cleaned_data)
            profile.save()
            return redirect('/user/me')
        else:
            return render(request, 'message.html', {'title': 'Failure', 'message': 'Failed to create profile.'})

class EditProfileView(View):
    def get(self, request, *args, **kwargs):
        form = CreateProfileForm(instance=request.user.profile)
        return render(request, 'form.html', {'form': form, 'title': 'Create Profile'})

    def post(self, request, *args, **kwargs):
        form = CreateProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid() and request.user.is_authenticated:
            form.save()
            return redirect('/user/me')
        else:
            return render(request, 'message.html', {'title': 'Failure', 'message': 'Failed to create profile.'})
