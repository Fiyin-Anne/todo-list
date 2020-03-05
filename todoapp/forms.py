from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        
class CreateUserForm(UserCreationForm): #createuserform is inheriting from usercreationform
    class Meta:
        model =  User
        fields = ['username', 'email', 'password1', 'password2']