from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        User,
        related_name='sender'
    )
    receivers = models.ManyToManyField(
        User,
        related_name='receivers'
    )
    date = models.DateField(
        auto_now=True
    )
