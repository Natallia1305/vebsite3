from main.forms import TaskForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task 

from .forms import TaskForm

def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': task, 'description': 'description' } )

def about(request):
    return render(request, 'main/about.html' )

def contact(request):
    return render(request, 'main/contact.html' )

def make(request):
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'main/make.html' )

 
