from django.conf.urls import include, url
from django.contrib import admin

from user_profile import urls as user_profile_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(user_profile_urls))
]
