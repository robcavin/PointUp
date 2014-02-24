from django.db import models
from django_facebook.models import FacebookCustomUser

class User(FacebookCustomUser):
    points = models.IntegerField(default=100)