from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from django.contrib.auth.models import User
from group.models import Group
from project.forms import ProjectForm
from sprint.models import Sprint, SprintTask
from project.models import Project
from sprint.forms import SprintForm
from task.forms import TaskForm
from task.models import Task, Status, Priority
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from django.contrib.auth.models import User
from group.models import Group
from project.forms import ProjectForm
from sprint.models import Sprint, SprintTask
from project.models import Project
from sprint.forms import SprintForm
from task.forms import TaskForm
from task.models import Task, Status, Priority


class TaskCreateView(CreateView):
    model = Sprint
    form_class = TaskForm
    template_name = 'task/create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(name=self.kwargs['project'])
        return context

    def form_valid(self, form):
        project = Project.objects.get(name=self.kwargs['project'])
        if form['status'].value == 0:
            messages.add_message(self.request, messages.ERROR, 'You need to select status!')
            context = {'form': TaskForm, 'project': project}
            return render(self.request, 'task/create_view.html', context)
        status = Status.objects.get(id=int(form['status'].value()))
        if form['priority'].value == 0:
            messages.add_message(self.request, messages.ERROR, 'You need to select status!')
            context = {'form': TaskForm, 'project': project}
            return render(self.request, 'task/create_view.html', context)
        priority = Priority.objects.get(id=int(form['priority'].value()))
        activeSprint = Sprint.objects.get(project=project, status=True)
        if not activeSprint:
            messages.add_message(self.request, messages.ERROR, 'No active sprint!')
            context = {'form':TaskForm, 'project':project}
            return render(self.request,'task/create_view.html', context )
        task = Task.objects.create(project=project, time=form['time'].value(), reporter=self.request.user,
                           description=form['description'].value(),
                           status=status,
                           priority=priority, name=form['name'].value())
        SprintTask.objects.create(sprint=activeSprint, task=task)
        redirect_url = reverse_lazy('project_detail', args=[self.kwargs['project']])
        return HttpResponseRedirect(redirect_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)