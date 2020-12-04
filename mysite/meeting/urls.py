from .views import CreateMeetingView, MeetingView, JoinMeetingView, EditMeetingView, EventListView
from django.urls import path

urlpatterns = [
    path('create/', CreateMeetingView.as_view()),
    path('<int:event_id>/', MeetingView.as_view()),
    path('<int:event_id>/join/', JoinMeetingView.as_view()),
    path('<int:event_id>/edit/', EditMeetingView.as_view()),
    path('find_event/', EventListView.as_view(), name='find_event'),
    path('event_view/', MeetingView.as_view(), name='event_view')

]