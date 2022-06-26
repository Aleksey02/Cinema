from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_author", "comment_text"]
        widgets = {
            "comment_text": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш комментарий'}),
            "comment_author": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'})}


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
