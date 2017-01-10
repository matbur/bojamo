from django.conf.urls import url

from sprint.views import SprintCreateView
from task.views import TaskCreateView
from .views import project_detail

urlpatterns = [
    url(r'^(?P<name>\w+)/$', project_detail, name='project_detail'),
    url(r'^(?P<project>\w+)/add/sprint$', SprintCreateView.as_view(), name='sprint_create_view'),
    url(r'^(?P<project>\w+)/add/task$', TaskCreateView.as_view(), name='task_create_view')
]
