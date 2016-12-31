from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=40, unique=True)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=40)
    permissions = models.PositiveSmallIntegerField(blank=True, default=1)
    url = models.CharField(max_length=80, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return '{} "{}" {}'.format(self.first_name, self.username, self.last_name)


class Group(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

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


class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)
    repository = models.CharField(max_length=80)
    url = models.CharField(max_length=80)


class UserProject(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    permissions = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ['user', 'project']


class Message(models.Model):
    content = models.TextField()
    date = models.DateField()


class UserMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)


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
    time = models.PositiveIntegerField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)
    reporter = models.ForeignKey(User)
    priority = models.ForeignKey(Priority)


class UserTask(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)

    class Meta:
        unique_together = ['user', 'task']


class Comment(models.Model):
    task = models.ForeignKey(Task)
    content = models.TextField()
    date = models.DateField(default=timezone.now)


class UserComment(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)

    class Meta:
        unique_together = ['user', 'comment']


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
