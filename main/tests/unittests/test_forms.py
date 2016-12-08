import unittest
from main.forms import *

""" Simple Unittest for form Resgistration and Login """
class TestPage(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        @unittest.mock.patch.object(RegistrationForm, 'clean_email')
        def test_clean_email(self, mock_clean_email):
            clean_email = unittest.mock.Mock(email = 'mbanks@email.com')
            clean_email.return_value = 'mbanks@email.com'
            self.assertEqual(clean_email.return_value, 'mbanks@email.com')

        @unittest.mock.patch.object(RegistrationForm, 'clean_email')
        def test_clean_username(self, mock_clean_username):
            clean_username = unittest.mock.Mock(username = 'mbanks')
            clean_username.return_value = 'mbanks'
            self.assertEqual(clean_username.return_value, 'mbanks')

        @unittest.mock.patch.object(RegistrationForm, 'clean_email')
        def test_clean_password(self, mock_clean_password):
            clean_password = unittest.mock.Mock(password = 'mbanks123')
            clean_password.return_value = 'mbanks123'
            self.assertEqual(clean_password.return_value, 'mbanks123')

        @unittest.mock.patch.object(RegistrationForm, 'clean_email')
        def test_clean_register(self, mock_clean_email):
            clean_register = unittest.mock.Mock(username = 'tbarnett',
                email = 'tbarnett@email.com', password = 'tbarnett123')
            clean_register.return_value = ('tbarnett', 'tbarnett@email.com',
                'tbarnett123')
            self.assertEqual(clean_register.return_value, ('tbarnett', 'tbarnett@email.com', 
                'tbarnett123'))

        @unittest.mock.patch.object(LoginForm, 'clean')
        def test_clean(self, mock_clean):
            clean = unittest.mock.Mock(username = 'mbanks', password = 'mbanks123')
            clean.return_value = ('mbanks', 'mbanks123')
            self.assertEqual(clean.return_value, ('mbanks', 'mbanks123'))

        @unittest.mock.patch.object(LoginForm, 'clean')
        def test_clean_bad(self, mock_clean):
            clean = unittest.mock.Mock(username = 'mbanks', password = 'mbanks123')
            clean.return_value = ('mbanks', 'mbanks123')
            self.assertNotEqual(clean.return_value, ('mmbanks', 'mbanks123'))
