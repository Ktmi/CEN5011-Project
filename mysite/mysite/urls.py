"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view,create_event_view,find_event_view,contact_view,login_view,sign_up_view,personal_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_event/', create_event_view, name='create_event'),
    path('find_event/', find_event_view, name='find_event'),
    path('faq/', faq_view, name='faq'),
    path('rules/', rules_view, name='rules'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('meet/', include('meeting.urls')),
    path('personal/',personal_view,name='personal')
]
