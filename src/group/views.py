from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, ListView

from .forms import GroupForm
from .models import Group, UserGroup


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/create_view.html'
    success_url = 'users_profile/loggedin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testowa_zmienna'] = ['1', '2', '3']
        return context


class GroupListView(ListView):
    model = Group


@login_required
def group_detail(request, name):
    group = get_object_or_404(Group, name=name)
    owner = User.objects.get(id=group.owner_id)
    members = [i.user for i in UserGroup.objects.filter(group=group)]
    context = {'group': group, 'owner': owner, 'members': members}
    return render(request, 'group/group_detail.html', context)
