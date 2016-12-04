""" Forms for the main app """

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext

class RegistrationForm(forms.ModelForm):
    """ Registration form for registering users """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    """ Login form form for users login """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        self._user = authenticate(username=username, password=password)
        if self._user is None:
            raise forms.ValidationError(ugettext("Invalid username or password"))
        return self.cleaned_data
