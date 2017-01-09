from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from django.contrib.auth.models import User
from group.models import Group
from project.forms import ProjectForm
from sprint.models import Sprint
from .models import Project, UserProject


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = Group.objects.get(name=self.kwargs['group'])
        return context

    def form_valid(self, form):
        group = Group.objects.get(name=self.kwargs['group'])
        project = Project.objects.create(owner=self.request.user, group=group, url=form['url'].value(), repository=form['repository'].value(), name=form['name'].value(), description=form['description'].value())
        print(project)
        UserProject.objects.create(user=self.request.user, project=project, permissions=9001)
        redirect_url = reverse_lazy('group_detail', args=[self.kwargs['group']])
        return HttpResponseRedirect(redirect_url)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)


@login_required
def project_detail(request, name):
    project = get_object_or_404(Project, name=name)
    group = Group.objects.get(id=project.group_id)
    owner = User.objects.get(id=project.owner_id)
    members = [i.user for i in UserProject.objects.filter(project=project)]
    sprints = Sprint.objects.filter(project=project)
    context = {'project': project, 'owner': owner, 'group': group, 'members': members, 'sprints': sprints}
    return render(request, 'project/project_detail.html', context)