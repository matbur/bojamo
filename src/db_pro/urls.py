from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.urls import include, url

from db_pro import settings
from group import urls as group_urls
from project import urls as project_urls
from user_profile import urls as user_profile_urls
from .views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'', include(user_profile_urls)),
    url(r'^group/', include(group_urls)),
    url(r'^project/', include(project_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^_debug/', include(debug_toolbar.urls)),
    ] + urlpatterns

