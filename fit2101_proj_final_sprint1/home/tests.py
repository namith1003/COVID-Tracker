from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Namith', 'namithspider@gmail.com', 'mypass')
        self.user.save()
        self.profile = Profile(self.user, "0123456789")
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.telephone = '0123456789'
        self.password = 'passwordForTesting'

    # tests if a newly created profile is of rank admin
    def test_profile_is_admin(self):
        user = User.objects.get(username='Namith')
        self.assertNotEqual(user.username, 'admin')

    def test_created_profile_exists(self):
        self.assertTrue(authenticate(username='Namith', password='mypass'))

    def test_password_change(self):
        user = User.objects.get(username='Namith')
        user.set_password('new mypass')
        user.save()
        self.assertEqual(user.check_password("new mypass"), True)

    def test_signup_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_page_view_name(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_form(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'tel': self.telephone,
            'password': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 2)
