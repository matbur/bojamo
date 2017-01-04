from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    url = models.URLField(
        max_length=80,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
