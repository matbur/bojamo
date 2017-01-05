from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.utils.http import is_safe_url
from group.models import Group


def login(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('loggedin'))

    context = {
        'messages': []
    }

    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)

        if user != None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('loggedin'))
            else:
                context['messages'].append('User is inactive!')
        else:
            context['messages'].append('Username or password is invalid!')

    context.update(csrf(request))
    return render_to_response(
        'user_profile/login.html',
        context
    )


def registration(request):
    ###TODO filtr fields if they contain default values!!!

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
                return render_to_response(
                    'user_profile/registration.html',
                    context
                )

        if user:
            context['messages'].append('This username already exitsts!')
        elif email:
            context['messages'].append('This email is in use!')
        elif form['password'] != form['confirm_password']:
            context['messages'].append('Password is invalid!')
        else:
            user = User.objects.create_user(first_name=form['first_name'],
                           last_name=form['last_name'],
                           email=form['email'],
                           username=form['username'],
                           password=form['password']
                           )
            auth.login(request, user)
            return HttpResponseRedirect(reverse_lazy('loggedin'))
    context.update(csrf(request))
    return render_to_response(
        'user_profile/registration.html',
        context
    )

@login_required
def loggedin(request):
    return render_to_response(
        'user_profile/loggedin.html'
    )
