from django.db import models

from project.models import Project
from task.models import Task


class Sprint(models.Model):
    project = models.ForeignKey(Project)
    begin = models.DateField()
    end = models.DateField()
    number = models.IntegerField()
    status = models.BooleanField()


class SprintTask(models.Model):
    sprint = models.ForeignKey(Sprint)
    task = models.ForeignKey(Task)
    time = models.IntegerField()

    def __str__(self):
        return '({}, {})'.format(self.user.username, self.task)
