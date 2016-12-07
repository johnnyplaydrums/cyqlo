from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
import main.views

"""
To run this test do the following :
python manage.py test tests.unittests.test_views

Updated!
We still use client but set it for response = self.client.get()
This is as close as we can get to pure unit testing with most recent
pull (12/6/2015).

The response.status_code checks if the url is 200 was successful in grabbing
the client response.

The assertContains is checking the base.html''s body for the following
<a href=""></a> and checks if the response has the information we are looking
at in the test.

The assertTemplateUsed() checks for asserts that the template with the given
name was used in rendering the response.
"""

class TestPage(TestCase):
    #Homepage
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_page(self):
        response = self.client.get('/login_view')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/login_view">Login</a>')
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_page(self):
        response = self.client.get('/logout_view')
        self.assertRedirects(response, '/')

    def test_signup_page(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
            '<a href="/signup" class="p-r-none">Sign Up</a>')
        self.assertTemplateUsed(response, 'signup.html')

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/about">About</a>')
        self.assertTemplateUsed(response, 'about.html')

    def test_route_page(self):
        response = self.client.get('/routes_page')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/routes_page">Routes</a>')
        self.assertTemplateUsed(response, 'routes.html')

    #Implement profile test
