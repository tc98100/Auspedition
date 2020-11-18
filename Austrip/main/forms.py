from profile import Profile

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserInfo, Recommendation, AttractionComment


class AddCommentDestination(ModelForm):
    class Meta:
        model = AttractionComment
        fields = ['comment_content']


class AddCommentAttraction(ModelForm):
    class Meta:
        model = AttractionComment
        fields = ['comment_content']


class EditRecommendation(ModelForm):
    class Meta:
        model = Recommendation
        fields = ['title', 'long_description', 'short_description', 'image']


class ChangeUserInfo(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ChangePicBio(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['bio', 'image']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Firstname'}),
        #     'last_name': forms.TextInput(attrs={'class': 'input'}),
        #     'password1': forms.TextInput(attrs={'class': 'input'}),
        #     'password2': forms.TextInput(attrs={'class': 'input'}),
        # }