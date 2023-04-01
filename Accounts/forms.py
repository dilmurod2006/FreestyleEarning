from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ('country','city','first_name','last_name','age','zipcode','phone_number','username','email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", 'email', 'phone_number', 'avatar')
