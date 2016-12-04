""" Forms for the main app """
#from django.forms import ModelForm
#from main.models import User

from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    """ Registration form for registering users """
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    class Meta:
        """ A meta class that get the fields from user models """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
