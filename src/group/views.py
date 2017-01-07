from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from project.models import Project
from .forms import GroupForm
from .models import Group, UserGroup


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/create_view.html'
    success_url = 'user_profile/loggedin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        group = Group.objects.create(owner=self.request.user, name=form['name'].value(), description=form['description'].value())
        UserGroup.objects.create(user=self.request.user, group=group)
        return HttpResponseRedirect(reverse_lazy('dashboard'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupCreateView, self).dispatch(*args, **kwargs)


class GroupListView(ListView):
    model = Group


@login_required
def group_detail(request, name):
    group = get_object_or_404(Group, name=name)
    owner = User.objects.get(id=group.owner_id)
    members = [i.user for i in UserGroup.objects.filter(group=group)]
    projects = Project.objects.filter(group=group)
    context = {'group': group, 'owner': owner, 'members': members, 'projects': projects}
    return render(request, 'group/group_detail.html', context)
