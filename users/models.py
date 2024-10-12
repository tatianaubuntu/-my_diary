from django.contrib.auth.models import AbstractUser
from django.db import models

from diary.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    firstname = models.CharField(max_length=35, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=35, verbose_name='фамилия', **NULLABLE)
    birthdate = models.DateField(verbose_name='дата рождения', **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
