from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        help_text="Username should have at least 10 letters",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your user name"}
        ), 
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        ),
    )
