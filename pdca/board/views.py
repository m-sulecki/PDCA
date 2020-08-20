from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

def home(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'board/home.html', context)

class TaskListView(ListView):
    model = Task
    template_name = 'board/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_notification']

class TaskDetailView(DetailView):
    model = Task


def about(request):
    return render(request, 'board/about.html', {'title': 'About'})
