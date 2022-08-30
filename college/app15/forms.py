from django import forms
from app15.models import Studreg
from app15.models import Empreg 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class Newstud(forms.ModelForm):
    class Meta():
        model=Studreg
        fields="__all__"


class Newemp(forms.ModelForm):
    class Meta():
        model=Empreg
        fields="__all__"


class loginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model=User
        fields=('username','email','password1','password2','is_admin','is_employee','is_customer')

       