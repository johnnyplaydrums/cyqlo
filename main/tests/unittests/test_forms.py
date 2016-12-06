from django.test import TestCase
from main.forms import RegistrationForm

class FormsTestPage(TestCase):

    def test_Melissa_form(self):
        form = RegistrationForm({'username': 'mbanks',
            'email': 'mbanks@email.com', 'password': 'mbanks123'})
        self.assertTrue(form.is_valid())
        register = form.save()
        self.assertEqual(register.username, 'mbanks')
        self.assertEqual(register.email, 'mbanks@email.com')
        self.assertEqual(register.password, 'mbanks123')

    def test_Tom_form(self):
        form = RegistrationForm({'username': 'tbarnett',
            'email': 'tbarnett@email.com', 'password': 'tbarnett123'})
        self.assertTrue(form.is_valid())
        register = form.save()
        self.assertEqual(register.username, 'tbarnett')
        self.assertEqual(register.email, 'tbarnett@email.com')
        self.assertEqual(register.password, 'tbarnett123')

    def test_blank_form(self):
        form = RegistrationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username' : ['This field is required.'],
            'email' : ['This field is required.'],
            'password' : ['This field is required.']
        })
