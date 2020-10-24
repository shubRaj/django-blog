from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"required":True,}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"required":True,}))
    email = forms.EmailField()
    class Meta:
        model = User
        fields =["first_name","last_name","username","email","password1","password2"]