from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from .forms import CreateAccountForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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


@login_required()
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,"personal.html",context)




