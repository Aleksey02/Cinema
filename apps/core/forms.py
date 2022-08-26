from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'user-box'}))
    email = forms.EmailField(label='Email', widget=forms.PasswordInput(attrs={'class': 'user-box'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'user-box'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'user-box'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'user-box'}))
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'user-box'}))
    class Meta:
        model = User
        fields = ['username', 'password']


class SearchForm(forms.Form):
    name_film = forms.CharField(label='Film name', max_length=100)