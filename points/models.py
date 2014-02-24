from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_facebook.models import FacebookModel


class CustomUser(AbstractUser, FacebookModel):
    objects = UserManager()
    state = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(default=100)
