from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=35)
    login = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    permission = models.PositiveSmallIntegerField()


class Group(models.Model):
    owner = models.IntegerField()
    name = models.CharField(max_length=50)
    date = models.DateField()


class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)


class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()


class UserProject(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    permissions = models.IntegerField()


class Message(models.Model):
    content = models.TextField()


class UserMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)


class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=50)


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


class SprintTask(models.Model):
    spring = models.ForeignKey(Sprint)
    task = models.ForeignKey(Task)
    time = models.IntegerField()
