from django.contrib.auth.models import User #gives generic user class
from django import forms

class UserForm(forms.ModelForm):    #blueprint for the registration form u r going to make
    password = forms.CharField(widget=forms.PasswordInput)  #widget is used to generate protection rather than showing plaintext password when user enters them

    class Meta:
        model = User
        fields = ['username','email','password']