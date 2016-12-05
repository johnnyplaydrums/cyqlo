""" Forms for the main app """
from django import forms

class RegistrationForm(forms.Form):
    """ Registration form for registering users """

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
