from django.shortcuts import render, redirect 
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
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

def deleteTask(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)