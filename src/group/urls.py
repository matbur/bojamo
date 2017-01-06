from django.conf.urls import url

from .views import GroupCreateView, group_detail

urlpatterns = [
    url(r'^create/$', GroupCreateView.as_view(), name='group_create_view'),
    url(r'^get/(\w+)', group_detail, name='group_detail'),
]
