from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(max_length=30, widget=forms.PasswordInput)
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('student_grade', 'student_group')


class RegisterForm(forms.ModelForm):
    student_grade = forms.IntegerField(help_text='Decimal.')

    class Meta:
        model = User
        fields = ('username', 'password', 'student_grade')
