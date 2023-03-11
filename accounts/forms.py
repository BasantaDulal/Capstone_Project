from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(eidget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)