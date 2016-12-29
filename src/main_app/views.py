from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PriorityForm, StatusForm, UserForm
from .models import User


def index(request):
    context = {
        'user_form': UserForm(),
        'status_form': StatusForm(),
        'priority_form': PriorityForm(),
    }
    return render(request, 'index.html', context)


def get_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def get_projects(request):
    return ''


def add_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')


def add_status(request):
    if request.method == 'POST':
        form = StatusForm(data=request.POST)

        if form.is_valid():
            print('status valid')
            form.save()
        else:
            print('status not valid')

        return HttpResponseRedirect('/')


def add_priority(request):
    if request.method == 'POST':
        form = PriorityForm(data=request.POST)

        if form.is_valid():
            print('priority valid')
            form.save()
        else:
            print('priority not valid')

        return HttpResponseRedirect('/')
