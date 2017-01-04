from django.conf.urls import url
from .views import GroupCreateView

urlpatterns = [
    url(r'^create/$', GroupCreateView.as_view(), name='group_create_view')
]
