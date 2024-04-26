from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework import generics
from organization.views import upload_csv, FilterOrganizations, user_list, add_user, delete_user


class UrlTests(TestCase):
    def setUp(self):
        # Initialize the Django test client
        self.client = Client()

    def test_url_is_accessible(self):
        url = reverse('upload_csv')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_url_resolves_to_view(self):
        # Define the URL pattern you want to test
        url = reverse('filter_organizations_api')

        # Use resolve() to match the URL to a view function
        resolver_match = resolve(url)

        # Assert that the resolved view function is an instance of generics.ListAPIView
        self.assertIsInstance(resolver_match.func.cls, generics.ListAPIView)

        # Alternatively, you can directly check if the resolved view function is FilterOrganizations
        self.assertEqual(resolver_match.func.cls, FilterOrganizations)

