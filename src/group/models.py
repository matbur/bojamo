from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    owner = models.ForeignKey(
        User
    )
    name = models.CharField(
        max_length=50
    )
    date = models.DateField(
        auto_now=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    permissions = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return '({}, {})'.format(self.user.username, self.group)

    class Meta:
        unique_together = ['user', 'group']
