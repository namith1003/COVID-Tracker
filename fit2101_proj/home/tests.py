from http import HTTPStatus

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client

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

    # Tests if a newly created profile is of rank admin
    def test_profile_is_admin(self):
        user = User.objects.get(username='Namith')
        self.assertNotEqual(user.username, 'admin')

    # Test if a created new account is added to the database and exists
    def test_created_profile_exists(self):
        self.assertTrue(authenticate(username='Namith', password='mypass'))
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test whether password is updated once changed
    def test_password_change(self):
        user = User.objects.get(username='Namith')
        user.set_password('new mypass')
        user.save()
        self.assertEqual(user.check_password("new mypass"), True)

    # Test if the signup page exists and does open and initiate properly
    def test_signup_page_url(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    # Test if a account created using the signup page is registered and does exist.
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

    # Test if an account created  with no username it returns a ValueError stating username
    # has not been provided and the account isn't registered and saved.
    def test_signup_missing(self):
        with self.assertRaises(ValueError):
            response = self.client.post('/register/', data={
                'username': '',
                'email': self.email,
                'tel': self.telephone,
                'password': self.password,
                'password2': self.password
            })

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test to ensure no accounts are created if the 2 passwords provided during
    # signup do not match, therefore is invalid
    def test_signup_mismatch_passwords(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': self.email,
            'tel': self.telephone,
            'password': self.password,
            'password2': 'mypass'
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test to ensure no accounts are created if the username provided has
    # already been registered with an already registered account, therefore is invalid.
    def test_signup_existing_username(self):
        response = self.client.post('/register/', data={
            'username': 'Namith',
            'email': self.email,
            'tel': self.telephone,
            'password': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test to ensure no accounts are created if the email provided has already
    # been registered with an already registered account, therefore is invalid.
    def test_signup_existing_email(self):
        response = self.client.post('/register/', data={
            'username': self.username,
            'email': 'namithspider@gmail.com',
            'tel': self.telephone,
            'password': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test if the login page exists and does open and initiate properly
    def test_login_page_url(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    # Test if a valid registered account does login successfully.
    def test_login_valid(self):
        c = Client()
        logged_in = c.login(username='Namith', password='mypass')
        self.assertTrue(logged_in)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test if an account with an unregistered and invalid username cannot
    # login successfully
    def test_login_invalid_username(self):
        c = Client()
        logged_in = c.login(username='failedUser', password='mypass')
        self.assertFalse(logged_in)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test if an account with a registered valid username but using an
    # invalid password cannot login successfully
    def test_login_invalid_password(self):
        c = Client()
        logged_in = c.login(username='Namith', password='failedpass')
        self.assertFalse(logged_in)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    # Test if logout functionality works once a valid user has logged in
    def test_logout(self):
        c = Client()
        logged_in = c.login(username='Namith', password='mypass')
        self.assertTrue(logged_in)

        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)

    # Test if a valid registered account does login successfully, through the login path from urls
    def test_login_function_valid(self):
        response = self.client.post('/login/', data={
            'username': 'Namith',
            'password': 'mypass',

        })
        self.assertEqual(response.status_code, 302)

    # Test if an account with an unregistered and invalid username cannot
    # login successfully, through the login path from urls
    def test_login_function_invalid_username(self):
        response = self.client.post('/login/', data={
            'username': 'FailureUser',
            'password': 'mypass',

        })
        self.assertEqual(response.status_code, 302)

    # Test if an account with a registered valid username but using an
    # invalid password cannot login successfully, through the login path from urls
    def test_login_function_invalid_password(self):
        response = self.client.post('/login/', data={
            'username': 'Namith',
            'password': 'FailurePass',

        })
        self.assertEqual(response.status_code, 302)

    # Test if the forgot password page exists and does open and initiate properly
    def test_forgot_password_page_url(self):
        response = self.client.post('/forget_password/', data={
            'email': 'namithspider@gmail.com'

        })
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='forgotpassword.html')

    # Tests if the forgot password page accepts a Valid email
    def test_forgot_password_valid(self):
        response = self.client.post('/forget_password/', data={
            'email': self.email,
        })
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.status_code, 200)
