from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import Todoform, CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login') 
def home(request):
    todos = Todo.objects.all() 

    form = Todoform()

    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todos':todos, 'form': form}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def editTask(request, pk):
    task = Todo.objects.get(id=pk)
    
    form = Todoform(instance=task)

    if request.method == 'POST':
        form = Todoform(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'edit_task.html', context)

@login_required(login_url='login')
# ensures that user is logged in 
# before they can perform any task on the site
def deleteTask(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)

def signup(request):
    if request.user.is_authenticated:
        #prevent user from manually going to registeration page
        #after they have logged in
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

    context = {'form':form}
    return render(request, 'signup.html', context)

