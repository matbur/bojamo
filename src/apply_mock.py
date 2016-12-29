#!/usr/bin/env python3

import json
import re

import django

django.setup()

from main_app.models import *


def mock_user():
    with open('mock_user.json') as f:
        for user in json.load(f):
            User(**user).save()


def mock_group():
    with open('mock_group.json') as f:
        for mock in json.load(f):
            owner = User.objects.get(pk=mock.pop('owner'))
            name = re.sub('\W', '', mock.pop('name'))
            Group(owner=owner, name=name, **mock).save()


def mock_user_group():
    with open('mock_user_group.json') as f:
        for mock in json.load(f):
            user = User.objects.get(pk=mock.pop('user'))
            group = Group.objects.get(pk=mock.pop('group'))
            UserGroup(user=user, group=group, **mock).save()


if __name__ == '__main__':
    mock_user()
    mock_group()
    mock_user_group()
