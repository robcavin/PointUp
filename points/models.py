from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_facebook.models import FacebookModel, FacebookUser
from django.conf import settings

class CustomUser(AbstractUser, FacebookModel):
    objects = UserManager()
    state = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(default=100)

    @property
    def name(self):
        return self.facebook_name


class Transaction(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='senders')
    receiver = models.ForeignKey(CustomUser, related_name='receivers')
    pending_receiver = models.ForeignKey(FacebookUser, related_name='pending_receivers')
    points = models.IntegerField()
    message = models.TextField()
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    image = models.ImageField(upload_to='images', width_field=image_width,height_field=image_height)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

