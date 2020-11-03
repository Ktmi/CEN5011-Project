from .views import CreateAccountView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create_account/', CreateAccountView.as_view(return_address='/auth/create_account/')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='/auth/login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='/auth/logout'),
]