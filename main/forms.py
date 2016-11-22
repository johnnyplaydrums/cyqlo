""" Forms for the main app """
from django.forms import ModelForm
from main.models import User

class RegistrationForm(ModelForm):
    """ Registration form for registering users """
    class Meta:
        """ A meta class that get the fields from user models """
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
