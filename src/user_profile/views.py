from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import csrf

from group.models import UserGroup
from project.models import UserProject


@login_required
def user_detail(request, username):
    # TODO: display groups which belongs to this user
    context = {}

    user = get_object_or_404(User, username=username)
    context['get_user'] = user
    user_groups = UserGroup.objects.filter(user=user)
    context['groupProjects'] = {}
    for user_group in user_groups:
        projects = UserProject.objects.filter(user=user, project__group=user_group.group)
        context['groupProjects'][user_group.group.name] = projects or None
    return render(
        request,
        'user_profile/user_detail.html',
        context
    )


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('dashboard'))

    context = {
        'messages': []
    }

    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('dashboard'))
            else:
                context['messages'].append('User is inactive!')
        else:
            context['messages'].append('Username or password is invalid!')

    context.update(csrf(request))
    return render(
        request,
        'user_profile/login.html',
        context
    )


def registration(request):
    # TODO filter fields if they contain default values!!!

    context = {
        'messages': []
    }
    form = {}

    if request.POST:
        form['first_name'] = request.POST.get('first_name', None)
        form['last_name'] = request.POST.get('last_name', None)
        form['email'] = request.POST.get('email', None)
        form['username'] = request.POST.get('username', None)
        form['password'] = request.POST.get('password', None)
        form['confirm_password'] = request.POST.get('confirm_password', None)

        user = User.objects.filter(username=form['username'])
        email = User.objects.filter(email=form['email'])

        context.update(csrf(request))
        for key, value in form.items():
            if value is None:
                context['messages'].append('Please fill all fields')
                context.update(csrf(request))
                return render(
                    request,
                    'user_profile/registration.html',
                    context
                )

        if user:
            context['messages'].append('This username already exists!')
        elif email:
            context['messages'].append('This email is in use!')
        elif form['password'] != form['confirm_password']:
            context['messages'].append('Password is invalid!')
        else:
            user = User.objects.create_user(
                first_name=form['first_name'],
                last_name=form['last_name'],
                email=form['email'],
                username=form['username'],
                password=form['password']
            )
            auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('loggedin'))
    context.update(csrf(request))
    return render(
        request,
        'user_profile/registration.html',
        context
    )


@login_required
def loggedin(request):
    return render(
        request,
        'user_profile/loggedin.html'
    )
