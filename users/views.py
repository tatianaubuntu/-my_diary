import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import RegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Отправка подтверждения регистрации по электронной почте"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/email-confirm/{token}'
        send_mail(
            'Регистрация "Мой дневник"',
            f'Для подтверждения регистрации перейдите по ссылке {url}',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Проверка электронной почты"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class GeneratePasswordView(PasswordResetView):
    """Класс генерации нового пароля"""
    form_class = PasswordResetForm
    template_name = 'users/generate.html'

    def form_valid(self, form):
        """Генерация нового пароля с отправкой по электронной почте"""
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(12)
                user.set_password(password)
                user.save()
                send_mail(
                    'Смена пароля "Мой дневник"',
                    f'Ваш новый пароль: {password}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    )
            return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    """Класс редактирования профиля"""
    model = User
    form_class = UserProfileForm

    def get_success_url(self):
        """Направляет на указанную страницу если форма валидна"""
        return reverse('users:profile', args=[self.kwargs.get('pk')])
