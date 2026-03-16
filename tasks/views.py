from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import TaskForm
from .models import Task, TaskGroup

def index(request):
    return render(request, 'index.html', { 'name': 'World' })


def task_list(request):
    tasks = Task.objects.all()
    taskgroups = TaskGroup.objects.all()
    form = TaskForm()
    ctx = { "task_list": tasks, "taskgroups": taskgroups, "form": form }
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('tasks:task_detail', pk=task.pk)
        return render(request, 'task_list.html', ctx)
    else:
        return render(request, 'task_list.html', ctx)


def task_detail(request, pk):
    ctx = { "task": Task.objects.get(pk=pk) }
    return render(request, 'task_detail.html', ctx)


class TaskDetailView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_detail.html"
    form_class = TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskgroups'] = TaskGroup.objects.all()
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_detail.html'
    form_class = TaskForm



# class TaskListView(TemplateView):
    # template_name = "task_list.html"

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['tasks'] = tasks
        # return context

    # def post(self, request, *args, **kwargs):
        # tasks.append(request.POST.get('task_name'))
        # context = self.get_context_data(**kwargs)
        # return self.get(request, *args, **kwargs)
