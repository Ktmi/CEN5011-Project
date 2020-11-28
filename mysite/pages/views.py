from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    home_context = {
        "nav": "home"
    }
    return render(request, "home.html", home_context)


def contact_view(request, *args, **kwargs):
    contact_context = {
        "nav" : "contact"
    }
    return render(request, "contact.html", contact_context)

def login_view(request, *args, **kwargs):
    login_context = {
        "nav" : "login"
    }
    return render(request, "login.html", login_context)

def sign_up_view(request, *args, **kwargs):
    sign_up_context = {
        "nav" : "sign_up"
    }
    return render(request, "sign_up.html", sign_up_context)

def faq_view(request, *args, **kwargs):
    faq_context = {
        "nav" : "faq"
    }
    return render(request, "faq.html", faq_context)

def rules_view(request, *args, **kwargs):
    rules_context = {
        "nav" : "rules"
    }
    return render(request, "rules.html", rules_context)

def personal_view(request, *args, **kwargs):
    personal_context ={
        "nav":"personal"
    }
    return render(request,"personal.html",personal_context)