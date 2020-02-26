from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home.html')
    return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request, 'login.html')    

def logout(request):
    pass



    