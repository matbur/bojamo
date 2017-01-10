from django.conf.urls import url

from sprint.views import SprintCreateView, sprint_detail_view
from task.views import TaskCreateView, task_detail_view
from .views import project_detail

urlpatterns = [
    url(r'^(?P<name>\w+)/$', project_detail, name='project_detail'),
    url(r'^(?P<project>\w+)/add/sprint$', SprintCreateView.as_view(), name='sprint_create_view'),
    url(r'^(?P<project>\w+)/add/task$', TaskCreateView.as_view(), name='task_create_view'),
    url(r'^(?P<project>\w+)/sprint/(?P<sprint>\w+)$', sprint_detail_view, name='sprint_detail_view'),
    url(r'^(?P<project>\w+)/sprint/(?P<sprint>\w+)/task/(?P<task>\w+)$', task_detail_view, name='task_detail_view'),
]
