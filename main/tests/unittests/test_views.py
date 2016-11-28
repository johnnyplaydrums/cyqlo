from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import main.views

class TestPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        #self.assertContains(response, 'Cyqlo')

    def test_login_page(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        #self.assertContains(response, 'Cyqlo')

    def test_signup_page(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_about_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_route_page(self):
        url = reverse('routes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'routes.html')
