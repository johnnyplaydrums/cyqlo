from django.test import TestCase
from main.forms import RegistrationForm

class FormsTestPage(TestCase):

    def test_Melissa_form(self):
        form = RegistrationForm({'first_name': 'Melissa', 'last_name': 'Banks', 'email': 'mbanks@email.com',
                'password': 'mbanks123'})
        self.assertTrue(form.is_valid())
        register = form.save()
        self.assertEqual(register.first_name, 'Melissa')
        self.assertEqual(register.last_name, 'Banks')
        self.assertEqual(register.email, 'mbanks@email.com')
        self.assertEqual(register.password, 'mbanks123')

    def test_Tom_form(self):
        form = RegistrationForm({'first_name': 'Tom', 'last_name': 'Barnett', 'email': 'tbarnett@email.com',
                'password': 'tbarnett123'})
        self.assertTrue(form.is_valid())
        register = form.save()
        self.assertEqual(register.first_name, 'Tom')
        self.assertEqual(register.last_name, 'Barnett')
        self.assertEqual(register.email, 'tbarnett@email.com')
        self.assertEqual(register.password, 'tbarnett123')

    def test_blank_form(self):
        form = RegistrationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'first_name' : ['This field is required.'],
            'last_name' : ['This field is required.'],
            'email' : ['This field is required.'],
            'password' : ['This field is required.']
        })
