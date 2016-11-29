from django.test import TestCase
from main.models import User

class FormsTestPage(TestCase):

    def setUp(self):
        self.jGlover=User.objects.create(first_name ="James", last_name="Glover", email="jglover@email.com",
                password="jglover123")
        self.aRamos=User.objects.create(first_name="Alyssa", last_name="Ramos", email="aramos@email.com",
                password="aramos123")

    def tearDown(self):
        pass

    def test_form_user(self):
        """
        Same as the test_models - Assert that the user James Glover was created
        """
        self.assertIsNotNone(self.jGlover)

    def test_form_username(self):
        """
        Same as the test_models - Asster that the user exist in the database
        """
        aRamos = User.objects.get(email = "aramos@email.com")
        self.assertEqual(self.aRamos, aRamos)

    def test_form_first_name(self):
        """
        Assert that first_name is less than the limit of 50
        """
        self.assertLess(len(self.jGlover.first_name),50)
        self.assertLess(len(self.aRamos.first_name),50)

    def test_form_last_name(self):
        """
        Assert that the last_name length is less than the limit of 50
        """
        self.assertLess(len(self.jGlover.last_name), 50)
        self.assertLess(len(self.aRamos.last_name), 50)

    def test_form_email(self):
        """
        Assert that the email length is less than the limit of 50
        """
        self.assertLess(len(self.jGlover.email), 50)
        self.assertLess(len(self.aRamos.email),50)

    def test_form_password(self):
        self.assertLess(len(self.jGlover.password), 256)
        self.assertLess(len(self.aRamos.password), 256)
