from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.utils.http import is_safe_url


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('loggedin'))

    args = {
        'next': request.GET.get('next', '') if request.GET else ''
    }

    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                if args['next'] and is_safe_url(url=args['next'], host=request.get_host):
                    return HttpResponseRedirect(args['next'])
                else:
                    return HttpResponseRedirect(reverse_lazy('loggedin'))
            else:
                messages.error(request, 'Użytkownik jest nieaktywny.')
        else:
            messages.error(request, 'Podano zły login lub hasło.')

    args.update(csrf(request))

    return render_to_response(
        'user_profile/login.html',
        context=args
    )


@login_required
def loggedin(request):
    return render_to_response(
        'user_profile/loggedin.html'
    )
