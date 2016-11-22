from django.test import TestCase
from main.models import User

class FormsTestPage(TestCase):

    def setUp(self):
        self.mBanks=User.objects.create(first_name ="James", last_name="Glover", email="jglover@email.com",
                password="jglover123")
        self.tBarnett=User.objects.create(first_name="Alyssa", last_name="Ramos", email="aramos@email.com",
                password="aramos123")
