from django.contrib.auth.models import User
from django.db import models

from task.models import Task


class Comment(models.Model):
    task = models.ForeignKey(Task)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{} | {}'.format(self.user.username, self.content)
