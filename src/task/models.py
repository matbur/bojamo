from django.contrib.auth.models import User
from django.db import models

from project.models import Project


class Status(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Statuses'


class Priority(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Priorities'


class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=14)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)
    reporter = models.ForeignKey(User)
    priority = models.ForeignKey(Priority)

    def __str__(self):
        return self.name


class UserTask(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)

    def __str__(self):
        return '({}, {})'.format(self.user.username, self.task)

    class Meta:
        unique_together = ['user', 'task']
