from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import LoginForm, PriorityForm, StatusForm, UserForm, UserRegistrationForm
from .models import Group, Project, User, UserGroup, UserProject, UserTask


def index(request):
    context = {
        'login_form': LoginForm(),
        # 'status_form': StatusForm(),
        # 'priority_form': PriorityForm(),
    }
    return render(request, 'main_app/index.html')#, context)


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
    return render(request, 'main_app/registration.html', context)


def user_login(request):
    context = {
        'login_form': LoginForm(),
    }
    request.session['user_id'] = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            print(form['username'])
            user = get_object_or_404(User.objects, username=str(form['username'].value()))
            request.session['user_id'] = user.id
            print('User verification successful')
            return dashboard(request)
        else:
            print('User verification unsuccessful')
            context['errors'] = form.errors
    return render(request, 'main_app/user_login.html', context)


def dashboard(request):
    print('dashboard')
    user_id = request.session.get('user_id', None)
    if not user_id:
        context = {'authorization': 'Authorization error! You have to be logged in!'}
        return render(request, 'main_app/dashboard.html', context)
    context = {'welcome': 'Welcome in bojamo project!' +str(user_id)}
    context['groups_member'] = [i.group for i in UserGroup.objects.filter(id=user_id)]
    context['user_projects'] = [i.project for i in UserProject.objects.filter(id=user_id)]
    context['user_tasks'] = UserTask.objects.filter(id=user_id)
    return render(request, 'main_app/dashboard.html', context)


def user_registration(request):
    context = {'user_registration_form': UserRegistrationForm()}
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            print('User verification successful')
            context['success'] = form._success
            form.save()
        else:
            print('User verification unsuccessful')
            context['errors'] = form.errors
        return render(request, 'main_app/registration.html', context)


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
