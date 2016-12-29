from django.contrib import admin

from .models import (
    Comment, Group, Message, Priority,
    Project, Sprint, Status, Task,
    User, UserComment, UserGroup, UserMessage,
    UserProject, UserTask
)

admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(Priority)
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(User)

admin.site.register(UserComment)
admin.site.register(UserGroup)
admin.site.register(UserMessage)
admin.site.register(UserProject)
admin.site.register(UserTask)
