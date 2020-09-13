from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class ExecutorForm(ModelForm):
    class Meta:
        model = Executor
        fields = '__all__'
        exclude = ['user']

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']