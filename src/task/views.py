from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from project.models import Project
from sprint.models import Sprint, SprintTask
from task.forms import TaskForm
from task.models import Priority, Status, Task


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
        active_sprint = Sprint.objects.get(project=project, status=True)
        if not active_sprint:
            messages.add_message(self.request, messages.ERROR, 'No active sprint!')
            context = {'form': TaskForm, 'project': project}
            return render(self.request, 'task/create_view.html', context)
        task = Task.objects.create(project=project, time=form['time'].value(), reporter=self.request.user,
                                   description=form['description'].value(),
                                   status=status,
                                   priority=priority, name=form['name'].value())
        SprintTask.objects.create(sprint=active_sprint, task=task)
        redirect_url = reverse_lazy('project_detail', args=[self.kwargs['project']])
        return HttpResponseRedirect(redirect_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)


@login_required
def task_detail_view(request, project, sprint, task):
    project = Project.objects.get(name=project)
    sprint = Sprint.objects.get(id=sprint)
    task = get_object_or_404(Task, id=task)
    reporter = User.objects.get(username=task.reporter)
    context = {'project': project, 'sprint': sprint, 'task': task, 'reporter': reporter}
    return render(request, 'task/task_detail.html', context)
