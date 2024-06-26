from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.forms import BooleanField

from catalog.forms import StyleFormMixin
from users.models import User
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRegisterFrom(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileFrom(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()