from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks' 


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo_app/task.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'todo_app/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'todo_app/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo_app/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')