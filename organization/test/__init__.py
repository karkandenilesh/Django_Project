from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        # Set up test data before each test method
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_user_creation(self):
        # Test whether the user was created successfully
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_authentication(self):
        # Test whether the user can be authenticated with the correct password
        user = User.objects.get(username='testuser')
        self.assertTrue(user.check_password('password123'))

    def test_user_str_method(self):
        # Test the string representation of the user
        self.assertEqual(str(self.user), 'testuser')  # Assuming the username is the expected string representation