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
from .models import Sprint
from project.models import Project
from .forms import SprintForm


class SprintCreateView(CreateView):
    model = Sprint
    form_class = SprintForm
    template_name = 'sprint/create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(name=self.kwargs['project'])
        return context

    def form_valid(self, form):
        project = Project.objects.get(name=self.kwargs['project'])
        projectSprints = Sprint.objects.filter(project=project)
        if projectSprints:
            latest = projectSprints.latest('begin')
            if not latest.status:
                num=latest.number+1
            else:
                messages.add_message(self.request, messages.ERROR, 'Latest sprint is still active!')
                context = {'form':SprintForm, 'project':project}
                return render(self.request,'sprint/create_view.html', context )
        else:
            num=1
        sprint = Sprint.objects.create(project=project, begin=form['begin'].value(), end=form['end'].value(), number=num ,status=True)
        print(sprint)
        redirect_url = reverse_lazy('project_detail', args=[self.kwargs['project']])
        return HttpResponseRedirect(redirect_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SprintCreateView, self).dispatch(*args, **kwargs)