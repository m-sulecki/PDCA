from django.urls import path
from .views import TaskListView, TaskDetailView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='board-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('about/', views.about, name='board-about'),
]