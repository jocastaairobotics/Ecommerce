from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLoginForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text="you password must contain min 1 capital, 1 small case, 1 symbol and 1 number \n Your password "
                  "length should be 8"
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text="Your password should be exact to password 1"
    )
