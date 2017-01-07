from django.conf.urls import url

from project.views import ProjectCreateView
from .views import GroupCreateView, group_detail

urlpatterns = [
    url(r'^create/$', GroupCreateView.as_view(), name='group_create_view'),
    url(r'^(?P<name>\w+)/$', group_detail, name='group_detail'),
    url(r'^(?P<group>\w+)/add/$', ProjectCreateView.as_view(), name='project_create_view'),
]
