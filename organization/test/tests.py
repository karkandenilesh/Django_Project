from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Organization, Profile

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



class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Set up test data before each test method
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.profile = Profile.objects.create(user=self.user, Address='Test Address', email='test@example.com', phone='1234567890', is_active=True, is_admin=False)

    def test_profile_creation(self):
        # Test whether the profile was created successfully
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.Address, 'Test Address')
        self.assertEqual(self.profile.email, 'test@example.com')
        self.assertEqual(self.profile.phone, '1234567890')
        self.assertTrue(self.profile.is_active)
        self.assertFalse(self.profile.is_admin)

    def test_profile_str_method(self):
        # Test the string representation of the profile
        self.assertEqual(str(self.profile), str(self.user))

class OrganizationModelTestCase(TestCase):
    def setUp(self):
        # Set up test data before each test method
        self.organization = Organization.objects.create(name='Test Organization', domain='test.com', year_founded=2020, industry='Test Industry', size_range='Small', locality='Test Locality', country='Test Country', linkedin_url='https://www.linkedin.com/', current_employee_estimate=10, total_employee_estimate=50)

    def test_organization_creation(self):
        # Test whether the organization was created successfully
        self.assertEqual(self.organization.name, 'Test Organization')
        self.assertEqual(self.organization.domain, 'test.com')
        self.assertEqual(self.organization.year_founded, 2020)
        self.assertEqual(self.organization.industry, 'Test Industry')
        self.assertEqual(self.organization.size_range, 'Small')
        self.assertEqual(self.organization.locality, 'Test Locality')
        self.assertEqual(self.organization.country, 'Test Country')
        self.assertEqual(self.organization.linkedin_url, 'https://www.linkedin.com/')
        self.assertEqual(self.organization.current_employee_estimate, 10)
        self.assertEqual(self.organization.total_employee_estimate, 50)

    def test_organization_str_method(self):
        # Test the string representation of the organization
        self.assertEqual(str(self.organization), 'Test Organization')