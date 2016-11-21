import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label=_("First Name"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label=_("Last Name"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=256, render_value=False)), label=_("Password"))

    def clean_email(self):
        '''
        Validate that the email is not already exist
        '''
        try:
            email = User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email you try to input already exists. Please try another one."))
