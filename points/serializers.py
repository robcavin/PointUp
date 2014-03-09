from models import CustomUser
from django.contrib.auth.models import Group
from rest_framework import serializers
from django_facebook.models import FacebookUser


class FacebookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')