""" Forms for the main app """
#from django.forms import ModelForm
#from main.models import User

from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    """ Registration form for registering users """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

class LoginForm(forms.Form):
    """ Registration form for registering users """
    username = forms.CharField(label="Username", widget=forms.TextInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
