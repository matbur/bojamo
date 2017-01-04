from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^users$', views.get_users, name='users'),
    url(r'^user/(\w+)$', views.get_user, name='get_user'),
    url(r'add_user$', views.add_user, name='add_user'),

    url(r'^registration$', views.registration, name='registration'),
    url(r'user_registration$', views.user_registration, name='user_registration'),
    url(r'^user_login$', views.user_login, name='user_login'),

    url(r'^dashboard$', views.dashboard, name='dashboard'),

    url(r'^groups$', views.get_groups, name='groups'),
    url(r'^group/(\w+)$', views.get_group, name='get_group'),

    url(r'^projects$', views.get_projects, name='projects'),
    url(r'^project/(\w+)$', views.get_project, name='get_project'),

    url(r'^sprints$', views.get_sprints, name='sprints'),
    url(r'^sprint/(\d+)$', views.get_sprint, name='get_sprint'),

    url(r'^tasks$', views.get_tasks, name='tasks'),
    url(r'^task/(\w+)$', views.get_task, name='get_task'),

    url(r'^comments$', views.get_comments, name='comments'),
    url(r'^comment/(\w+)$', views.get_comment, name='get_comment'),

    url(r'add_status$', views.add_status, name='add_status'),
    url(r'add_priority$', views.add_priority, name='add_priority'),

    url(r'^projects$', views.get_projects, name='projects'),
]
