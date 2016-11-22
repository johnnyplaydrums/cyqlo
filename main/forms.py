from django.forms import ModelForm
from main.models import User

""" Registration form for registering users """
class RegistrationForm(ModelForm):
    # A meta class that get the fields from user models
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
