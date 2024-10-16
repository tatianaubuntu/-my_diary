from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.core.exceptions import ObjectDoesNotExist

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


class YourPasswordResetForm(PasswordResetForm):

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        try:
            email = self.cleaned_data.get('email')
            user = User.objects.get(email=email)
            if user:
                return user
        except ObjectDoesNotExist:
            raise forms.ValidationError('Данный email не зарегистрирован')
