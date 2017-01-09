from django.conf.urls import url

from sprint.views import SprintCreateView
from .views import project_detail

urlpatterns = [
    url(r'^(?P<name>\w+)/$', project_detail, name='project_detail'),
    url(r'^(?P<project>\w+)/add$', SprintCreateView.as_view(), name='sprint_create_view')
]
