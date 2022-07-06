from random import choices
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import VISIT_LENGTH_CHOICES

class MyDateInput(forms.DateTimeInput):
    input_type='date'

class Login_form(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=50, widget=forms.PasswordInput)

class Register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
class Length_visit_form(forms.Form):
    Visit_length=forms.ChoiceField(choices=VISIT_LENGTH_CHOICES)

class Day_of_visit(forms.Form):
    Day=forms.DateField(widget=MyDateInput)