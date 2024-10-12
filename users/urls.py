from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import GeneratePasswordView, RegisterView, email_verification, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html', next_page='diary:entries'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('generate/', GeneratePasswordView.as_view(), name='generate'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
