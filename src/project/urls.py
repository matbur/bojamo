from django.conf.urls import url

from .views import project_detail

urlpatterns = [
    url(r'^(?P<name>\w+)/$', project_detail, name='project_detail'),
]
