from django.shortcuts import render

from .models import User


def index(request):
    return render(request, 'index.html')


def get_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def get_projects(request):
    return ''
