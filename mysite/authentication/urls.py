from .views import CreateAccountView
from django.urls import path

urlpatterns = [
    path('create_account/', CreateAccountView.as_view(return_address='/auth/create_account/')),
]