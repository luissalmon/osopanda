from django import forms
from bsite.models import User, Person

class Person_Form(forms.Form):
    username = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    birthDate = forms.DateField(required=False)
    mail = forms.EmailField(required=False)
    password = forms.CharField(max_length=20)
    passwordConfirmation = forms.CharField(max_length=20)
