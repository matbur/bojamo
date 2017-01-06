from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexView

from user_profile import urls as user_profile_urls
from group import urls as group_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'', include(user_profile_urls)),
    url(r'^group/', include(group_urls))
]
