from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task
from .forms import PositionForm

from django.contrib.auth import logout


# Create your views here.

class CustomLoginView(LoginView):

    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class MyLogoutView(LogoutView):

    template_name = 'todo_app/logout.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def logout_view(request):
        logout(request)
        # Redirect to a success page.
    
    def get_success_url(self):
        return reverse_lazy('tasks')



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

class RegisterPage(FormView):
    template_name = 'todo_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                for id, position in form.cleaned_data.items():
                    Task.objects.filter(id=id).update(position=position)
        return redirect('tasks')