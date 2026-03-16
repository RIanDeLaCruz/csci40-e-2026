from django.urls import path

from .views import (
    index, task_list,  task_detail,
    TaskDetailView, TaskListView, TaskCreateView
)

urlpatterns = [
    path('', index, name='index'),
    path('create', TaskCreateView.as_view(), name='task-create'),
    path('list', TaskListView.as_view(), name='task-list'),
    path('<int:pk>', TaskDetailView.as_view(), name='task_detail'),
]

app_name = 'tasks'
