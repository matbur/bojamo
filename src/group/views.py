from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Group
from .forms import GroupForm


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group/create_template.html'
    success_url = 'users_profile/loggedin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testowa_zmienna'] = ['1', '2', '3']
        return context


class GroupListView(ListView):
    model = Group
