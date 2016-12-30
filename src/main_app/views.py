from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import PriorityForm, StatusForm, UserForm
from .models import Group, Project, User, UserGroup, UserProject, UserTask


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


def get_user(request, name):
    user = get_object_or_404(User.objects, username=name)
    groups_owner = Group.objects.filter(owner=user)
    groups_member = [i.group for i in UserGroup.objects.filter(user=user)]
    tasks = UserTask.objects.filter(user=user)
    context = {'user': user, 'groups_owner': groups_owner, 'groups_member': groups_member, 'tasks': tasks}
    return render(request, 'user.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')


def get_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def get_group(request, name):
    group = get_object_or_404(Group.objects, name=name)
    members = [i.user for i in UserGroup.objects.filter(group=group)]
    context = {'group': group, 'members': members}
    return render(request, 'group.html', context)


def get_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def get_project(request, name):
    project = get_object_or_404(Project.objects, name=name)
    users = [i.user for i in UserProject.objects.filter(project=project)]
    context = {'project': project, 'users': users}
    return render(request, 'project.html', context)


def get_sprints(request):
    # sprints = Sprint.objects.all()
    # return render(request, 'sprints.html', {'sprints': sprints})
    return render(request, 'sprints.html')


def get_sprint(request, num):
    # sprint = get_object_or_404(Sprint.objects, pk=num)
    # context = {'sprint': sprint}
    # return render(request, 'sprint.html', context)
    return render(request, 'sprint.html')


def get_tasks(request):
    return render(request, 'tasks.html')


def get_task(request):
    return render(request, 'task.html')


def get_comments(request):
    return render(request, 'comments.html')


def get_comment(request):
    return render(request, 'comment.html')


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
