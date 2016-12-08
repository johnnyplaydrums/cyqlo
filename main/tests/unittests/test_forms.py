import unittest
from main.forms import *

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
