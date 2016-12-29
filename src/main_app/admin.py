from django.contrib import admin

from .models import Priority, Status, User

admin.site.register(User)
admin.site.register(Status)
admin.site.register(Priority)
