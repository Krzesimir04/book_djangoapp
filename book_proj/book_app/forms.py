import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class MyDateInput(forms.DateTimeInput):
    input_type='date'

class Login_form(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=50, widget=forms.PasswordInput)

class Register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Day_of_visit(forms.Form):
    Day=forms.DateField(widget=MyDateInput)

    def clean_Day(self):
        Day=self.cleaned_data.get('Day')
        if Day<=datetime.datetime.now().date():
            raise forms.ValidationError('You have to choose the future date')
        if (Day-datetime.datetime.now().date()).days>=92:
            raise forms.ValidationError('You must book your visit earlier (max 3 months since today)')
        else:
            return Day