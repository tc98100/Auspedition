from django.apps import AppConfig
from django.test import TestCase

from main.forms import CreateUserForm


class TestForms(TestCase):
    def test_same_password_valid(self):
        form = CreateUserForm(data={
            'username': 'jae',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'superstrong123',
            'password2': 'superstrong123'
        })

        self.assertTrue(form.is_valid())