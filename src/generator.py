from datetime import date
from random import choice, random, randint

import django
import os

from django.contrib.auth.hashers import make_password

os.environ['DJANGO_SETTINGS_MODULE'] = 'db_pro.settings'
django.setup()


from group.models import UserGroup, Group
from user_profile.models import UserProfile, User
from project.models import Project, UserProject
from sprint.models import Sprint, SprintTask
from task.models import Task, Status, Priority, UserTask
from comment.models import Comment


NAME="USER"
GROUP="TEST_GROUP_"
PROJECT="PRO_TEST_"
SPRINT="SPRINT_"

def generate_user(name):
    usr = User(
        username=NAME+name,
        password=make_password('qwerty123'),
        email=name+"@bojamo.com"
    )
    usr.save()
    prof = UserProfile(user=usr)
    prof.save()
    return prof

def generate_group(name):
    g = Group(
        owner=choice(User.objects.all()),
        name=GROUP+name,
    )
    g.save()
    UserGroup(
        user=g.owner,
        group=g,
    ).save()
    return g

def user_to_group():
    g = -1
    for usr in User.objects.all():
        g = choice(Group.objects.all())
        if UserGroup.objects.filter(user=usr, group=g).first():
            continue
        UserGroup(
            group=g,
            user=usr
        ).save()

def generate_projects(name):
    g = choice(Group.objects.all())
    usr = choice(UserGroup.objects.filter(group=g)).user
    p = Project(
        group=g,
        owner=usr,
        name=PROJECT+name,
        repository="SOME_REPO.COM"+name,
        url="SOME_WWW"+name,
    )
    p.save()
    UserProject(
        permissions=1,
        user=usr,
        project=p
    ).save()

def user_to_project():
    p = -1
    g = -1
    for usr in User.objects.all():
        g = UserGroup.objects.filter(user=usr).first()
        print(g)
        if not g:
            continue
        g=g.group
        p = Project.objects.filter(group=g).first()
        if not p:
            continue
        if UserProject.objects.filter(user=usr, project=p).first():
            continue
        UserProject(
            permissions=1,
            project=p,
            user=usr
        ).save()

def generate_sprint():
    for pro in Project.objects.all():
        for x in range(1, 12):
            Sprint(
                project=pro,
                begin=date(3000,x,1),
                end=date(3000,x,27),
                number=x,
                status=False if x !=0 else True
            ).save()

def generate_status():
    for s in range(0, 10):
        Status(
            name="STATUS_"+str(s),
        ).save()

def generate_priority():
    for s in range(0, 10):
        Priority(
            name="PRIORITY_"+str(s),
        ).save()

def generate_tasks():
    for pro in Project.objects.all():
        for p in range(0, 300):
            Task(
                project=pro,
                name=pro.name+"_TASK_"+str(p),
                status=choice(Status.objects.all()),
                priority=choice(Priority.objects.all()),
                reporter=choice(UserProject.objects.filter(project=pro)).user,
                time=randint(1, 100),
            ).save()

def task_to_sprint():
    for s in Sprint.objects.all():
        t = choice(Task.objects.filter(project=s.project))
        if randint(0,1):
            continue
        SprintTask(
            sprint=s,
            task=t
        ).save()

def task_to_user():
    for s in Sprint.objects.all():
        if 1 != s.number:
            continue
        u = choice(UserProject.objects.filter(project=s.project)).user
        for x in range(1, randint(2, 5)):
            t = None
            while(True):
                t = choice(Task.objects.all())
                if not UserTask.objects.filter(task=t).first():
                    break
            UserTask(
                task=t,
                user=u
            ).save()

def generate_comments():
    for t in Task.objects.all():
        if randint(0,1):
          continue
        for _ in range(0, randint(0,5)):
            u = choice(UserProject.objects.filter(project=t.project)).user
            c = ''
            for _ in range(0, randint(1, 10)):
                c+="Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
                   "Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi. Cras vel lorem. "
            Comment(
                user=u,
                task=t,
                content=c
            ).save()


if __name__ == "__main__":
    # for x in range(0, 1000):
    #     generate_user(str(x))
    # for x in range(0, 62):
    #     generate_group(str(x))
    # user_to_group()
    # for x in range(0, 120):
    #     generate_projects(str(x))
    #user_to_project()
    #generate_sprint()
    #generate_status()
    #generate_priority()
    #generate_tasks()
    task_to_user()
    generate_comments()