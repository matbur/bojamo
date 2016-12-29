from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^users$', views.get_users, name='users'),
    url(r'^user/(\w+)/', views.get_user, name='get_user'),
    url(r'^groups$', views.get_groups, name='groups'),
    url(r'^group/(\w+)/', views.get_group, name='get_group'),

    url(r'add_user/', views.add_user, name='add_user'),
    url(r'add_status/', views.add_status, name='add_status'),
    url(r'add_priority/', views.add_priority, name='add_priority'),


    url(r'^projects$', views.get_projects, name='projects'),
]
