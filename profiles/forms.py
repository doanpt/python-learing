from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'data-id': 1000}))
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
        field_classes = {'username': UsernameField}
        # widgets = {'email': forms.EmailInput(attrs={'required': True})}
