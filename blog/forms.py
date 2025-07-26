from django import forms
from .models import CustomUser, Post
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "thumbnail"]
