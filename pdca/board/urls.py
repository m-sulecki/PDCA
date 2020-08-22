from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='board-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('about/', views.about, name='board-about'),
]