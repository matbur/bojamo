from django.shortcuts import render


def index(request):
    return render(request, 'react_app/index.html')


def login_view(request):
    return render(request, 'react_app/login.html')
