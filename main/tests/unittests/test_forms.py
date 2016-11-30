from django.test import TestCase
from main.forms import RegistrationForm
from main.models import User

class FormsTestPage(TestCase):

    def test_Melissa_form(self):
        mel = User(first_name ="Melissa", last_name="Banks", email="mbanks@email.com",
                password="mbanks123")
        mel_form = RegistrationForm({'first_name': 'Melissa', 'last_name': 'Banks', 'email': 'mbanks@email.com',
                'password': 'mbanks123'}, instance = mel)
        self.assertEqual(mel_form.is_valid(), True)

    def test_Tom_form(self):
        tom = User(first_name ="Tom", last_name="Barnett", email="tbarnett@email.com",
                password="tbarnett123")
        tom_form = RegistrationForm({'first_name': '', 'last_name': 'Barnett', 'email': 'tbarnett@email.com',
                'password': 'tbarnett123'}, instance = tom)
        self.assertEqual(tom_form.is_valid(), False)
