from django.forms import Field
from django.test import TestCase

from main.forms import CreateUserForm
from main.forms import ChangeUserInfo
from main.forms import ChangePicBio
from main.forms import AddCommentAttraction
from main.forms import EditRecommendation


class UserTest(TestCase):

    def test_valid_sign_up(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'super_strong123',
            'password2': 'super_strong123'
        })
        self.assertTrue(form.is_valid())

    def test_username_invalid(self):
        form = CreateUserForm(data={
            'username': 'jane doe',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'super_strong123',
            'password2': 'super_strong123'
        })
        self.assertFalse(form.is_valid())

    def test_fields_required(self):
        form = CreateUserForm(data={
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, [str(Field.default_error_messages['required'])])
        self.assertEqual(form['password2'].errors, [str(Field.default_error_messages['required'])])

    def test_user_exists(self):
            form = CreateUserForm(data={
                'username': 'jane',
                'first_name': 'doe',
                'last_name': 'doe',
                'password1': 'super_strong123',
                'password2': 'super_strong123'
            })
            self.assertTrue(form.is_valid())

    def test_password_same(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'super_strong123',
            'password2': 'super_strong123'
        })
        self.assertTrue(form.is_valid())

    def test_password_different(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'super_strong123',
            'password2': 'f'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form["password2"].errors, [str(form.error_messages['password_mismatch'])])

    def test_password_too_common(self):
        form = CreateUserForm(data={
            'username': 'jane_doe',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())

    def test_password_too_short(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'short',
            'password2': 'short'
        })
        self.assertFalse(form.is_valid())

    def test_password_similar(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': 'janedoe',
            'password2': 'janedoe'
        })
        self.assertFalse(form.is_valid())

    def test_password_entirely_numeric(self):
        form = CreateUserForm(data={
            'username': 'jane',
            'first_name': 'doe',
            'last_name': 'doe',
            'password1': '1234567890',
            'password2': '1234567890'
        })
        self.assertFalse(form.is_valid())


class ChangePicBioTest(TestCase):

    def user_change_bio(self):
        form = ChangePicBio(data={
            'bio': 'some bio',
            'image': 'test.png'
        })
        self.assertTrue(form.has_changed())
        self.assertTrue(form.is_valid())


class ChangeUserInfoTest(TestCase):

    def user_change_info(self):
        form = ChangeUserInfo(data={
            'first_name': 'jane',
            'last_name': 'doe',
            'email': 'email'
        })
        self.assertTrue(form.is_valid())


class EditRecommendationTest(TestCase):

    def edit_recommendation(self):
        form = EditRecommendation(data={
            'title': 'some title',
            'long_description': 'very long description',
            'short_description': 'short description',
            'image': 'test.png'
        })
        self.assertTrue(form.is_valid())


class AddCommentAttractionTest(TestCase):

    def add_comment_attraction(self):
        form = AddCommentAttraction(data={
            'comment': 'some comment'
        })
        self.assertTrue(form.is_valid())


class AddCommentDestinationTest(TestCase):

    def add_comment_destination(self):
        form = AddCommentDestination(data={
            'comment': 'some comment'
        })
        self.assertTrue(form.is_valid())