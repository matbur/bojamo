from django.contrib.auth.models import User
from django.db import models

from group.models import Group


class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    repository = models.CharField(max_length=80)
    url = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    permissions = models.PositiveSmallIntegerField()

    def __str__(self):
        return '({}, {})'.format(self.user.username, self.group)

    class Meta:
        unique_together = ['user', 'project']
