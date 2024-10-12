from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'firstname', 'last_name', 'birthdate',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
