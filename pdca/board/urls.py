from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView
)
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='board-home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('about/', views.about, name='board-about'),
]