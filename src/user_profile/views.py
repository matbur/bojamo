from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.utils.http import is_safe_url


def login(request):
    messagealert = []
    mess = get_messages(request)

    for message in mess:
        print(message)
        messagealert.append(message)

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('loggedin'))

    #args = {
    #    'next': request.GET.get('next', '') if request.GET else ''
    #}

    context = {
        'messages' : []
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


@login_required
def loggedin(request):
    return render_to_response(
        'user_profile/loggedin.html'
    )
