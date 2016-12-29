from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.get_users, name='users'),
    url(r'^projects$', views.get_projects, name='projects'),
]
