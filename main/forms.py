""" Forms for the main app """

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    """ Registration form for registering users """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    """ Login form form for users login """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
