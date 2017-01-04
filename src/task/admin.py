from django.contrib import admin

from .models import Priority, Status, Task, UserTask

admin.site.register(Task)
admin.site.register(UserTask)
admin.site.register(Priority)
admin.site.register(Status)
