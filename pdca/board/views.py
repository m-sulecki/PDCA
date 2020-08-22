from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'

    def form_valid(self, form):
        form.instance.in_charge = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = '__all__'

    def form_valid(self, form):
        form.instance.in_charge = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.in_charge:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.in_charge:
            return True
        return False


def about(request):
    return render(request, 'board/about.html', {'title': 'About'})
