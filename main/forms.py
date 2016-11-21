from django.forms import ModelForm
from main.models import User

class RegistrationForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
