#!/usr/bin/env python3

import json
import os
import re

from django.db.utils import IntegrityError

os.environ['DJANGO_SETTINGS_MODULE'] = 'db_pro.settings'

import django

django.setup()

from main_app.models import *


def mock_user():
    with open('mock_user.json') as f:
        for mock in json.load(f):
            try:
                User(**mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_group():
    with open('mock_group.json') as f:
        for mock in json.load(f):
            owner = User.objects.get(pk=mock.pop('owner'))
            name = re.sub('\W', '', mock.pop('name'))
            try:
                Group(owner=owner, name=name, **mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_user_group():
    with open('mock_user_group.json') as f:
        for mock in json.load(f):
            user = User.objects.get(pk=mock.pop('user'))
            group = Group.objects.get(pk=mock.pop('group'))
            try:
                UserGroup(user=user, group=group, **mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_status():
    with open('mock_status.json') as f:
        for mock in json.load(f):
            try:
                Status(**mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_priority():
    with open('mock_priority.json') as f:
        for mock in json.load(f):
            try:
                Priority(**mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_project():
    with open('mock_project.json') as f:
        for mock in json.load(f):
            try:
                group = Group.objects.get(id=mock.pop('group'))
                Project(group=group, **mock).save()
            except IntegrityError as err:
                print(err, mock)


def mock_task():
    with open('mock_task.json') as f:
        for mock in json.load(f):
            try:
                project = Project.objects.get(id=mock.pop('project'))
                reporter = User.objects.get(id=mock.pop('reporter'))
                status = Status.objects.get(id=mock.pop('status'))
                priority = Priority.objects.get(id=mock.pop('priority'))
                Task(project=project, reporter=reporter, status=status,
                     priority=priority, **mock).save()
            except IntegrityError as err:
                print(err, mock)


if __name__ == '__main__':
    mock_user()
    mock_group()
    mock_user_group()
    mock_status()
    mock_priority()
    mock_project()
    mock_task()
