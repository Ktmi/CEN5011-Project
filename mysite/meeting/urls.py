from .views import CreateMeetingView
from django.urls import path

urlpatterns = [
    path('create/', CreateMeetingView.as_view()),
]