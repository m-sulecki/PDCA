from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'board/about.html', {'title': 'About'})
