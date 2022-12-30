import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyDateInput(forms.DateTimeInput):
    input_type='date'

class MyTimeInput(forms.DateTimeInput):
    input_type='time'

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
        if Day>datetime.datetime.now().date():
            return Day
        else:
            raise forms.ValidationError('You have to choose the future date')
class Reservation_form(forms.Form):
    Term=forms.TimeField(widget=MyTimeInput)