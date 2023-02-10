from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, PasswordResetForm

from base.form import StyleFormMixin
from users.models import User


class SigninForm(StyleFormMixin, AuthenticationForm):
    pass


class SignupForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"username": UsernameField}


class CustomPasswordResetForm(StyleFormMixin, PasswordResetForm):
    pass
