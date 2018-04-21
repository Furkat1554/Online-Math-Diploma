
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('student_grade','student_group')

class RegisterForm(forms.ModelForm):
    student_grade = forms.IntegerField(help_text='Decimal.')
    class Meta:
        model = User
        fields = ('username','password','student_grade')
