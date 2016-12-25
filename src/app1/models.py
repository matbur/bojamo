from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    login = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    permission = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=80)
    description = models.TextField()
    activated = models.BooleanField()

class Group(models.Model):
    owner = models.IntegerField()
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()

class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    permission = models.PositiveSmallIntegerField()

class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    repository = models.CharField(max_length=80)
    url = models.CharField(max_length=80)

class UserProject(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    permission = models.PositiveSmallIntegerField()

class Message(models.Model):
    content = models.TextField()
    date = models.DateField()

class UserMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)

class Status(models.Model):
    name = models.CharField(max_length=20)

class Priority(models.Model):
    name = models.CharField(max_length=20)

class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=50)
    time = models.PositiveIntegerField()
    description = models.TextField()
    status = models.ForeignKey(Status)
    reporter = models.ForeignKey(User)
    priority = models.ForeignKey(Priority)

class UserTask(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)

class Comment(models.Model):
    task = models.ForeignKey(Task)
    content = models.TextField()
    date = models.DateField()

class UserComment(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)

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
