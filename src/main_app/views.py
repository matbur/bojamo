from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import PriorityForm, StatusForm, UserForm, UserRegistrationForm
from .models import Group, Project, User, UserGroup, UserProject, UserTask


def index(request):
    context = {
        'user_form': UserForm(),
        'status_form': StatusForm(),
        'priority_form': PriorityForm(),
    }
    return render(request, 'main_app/index.html', context)

def get_users(request):
    users = User.objects.all()
    return render(request, 'main_app/users.html', {'users': users})


def get_user(request, name):
    user = get_object_or_404(User.objects, username=name)
    groups_owner = Group.objects.filter(owner=user)
    groups_member = [i.group for i in UserGroup.objects.filter(user=user)]
    tasks = UserTask.objects.filter(user=user)
    context = {'user': user, 'groups_owner': groups_owner, 'groups_member': groups_member, 'tasks': tasks}
    return render(request, 'main_app/user.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')


def get_groups(request):
    groups = Group.objects.all()
    return render(request, 'main_app/groups.html', {'groups': groups})


def get_group(request, name):
    group = get_object_or_404(Group.objects, name=name)
    members = [i.user for i in UserGroup.objects.filter(group=group)]
    context = {'group': group, 'members': members}
    return render(request, 'main_app/group.html', context)


def get_projects(request):
    projects = Project.objects.all()
    return render(request, 'main_app/projects.html', {'projects': projects})


def get_project(request, name):
    project = get_object_or_404(Project.objects, name=name)
    users = [i.user for i in UserProject.objects.filter(project=project)]
    context = {'project': project, 'users': users}
    return render(request, 'main_app/project.html', context)


def get_sprints(request):
    # sprints = Sprint.objects.all()
    # return render(request, 'sprints.html', {'sprints': sprints})
    return render(request, 'main_app/sprints.html')


def get_sprint(request, num):
    # sprint = get_object_or_404(Sprint.objects, pk=num)
    # context = {'sprint': sprint}
    # return render(request, 'sprint.html', context)
    return render(request, 'main_app/sprint.html')


def get_tasks(request):
    return render(request, 'main_app/tasks.html')


def get_task(request):
    return render(request, 'main_app/task.html')


def get_comments(request):
    return render(request, 'main_app/comments.html')


def get_comment(request):
    return render(request, 'main_app/comment.html')


def registration(request):
    context = {
        'user_registration_form': UserRegistrationForm()
    }
    return render(request, 'registration.html', context)


def user_registration(request):
    context = { 'user_registration_form': UserRegistrationForm()}
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            print('User verification successful')
            context['success'] = form._success
            form.save()
        else:
            print('User verification unsuccessful')
            context['errors']=form.errors
        return render(request, 'registration.html', context)


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
