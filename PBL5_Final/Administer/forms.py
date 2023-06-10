from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1','password2')
        
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={
        "class" : "form-control"
    }))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class" : "form-control"
    }))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class" : "form-control"
    }))
    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "class" : "form-control"
    }))
    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "class" : "form-control"
    }))
