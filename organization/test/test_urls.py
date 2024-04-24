from django.test import TestCase
from django.urls import reverse, resolve
from organization.views import upload_csv, FilterOrganizations, user_list, add_user, delete_user


class TestUrls(TestCase):

    def test_list_url_is_resolved(self):
        url = reverse('user_list')
        self.assertEqual(resolve(url).func, user_list)
