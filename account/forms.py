from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username =forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter your name"}))
    password =forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"}))

class RegForm(UserCreationForm):

    class Meta:

        model=User
        fields=['first_name','last_name','username','email','password1','password2']