from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Namith', 'namithspider@gmail.com', 'mypass')
        self.user.save()
        self.profile = Profile(self.user, "0123456789")

    # tests if a newly created profile is of rank admin
    def test_profile_is_admin(self):
        self.assertNotEqual(self.profile.user.username, 'admin')

    def test_created_profile_exists(self):
        self.assertTrue(authenticate(username='Namith', password='mypass'))

    def test_password_change(self):
        self.user.set_password('new mypass')
        self.user.save()
        self.assertEqual(self.user.password, 'new mypass')
