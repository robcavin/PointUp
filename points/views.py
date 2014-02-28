from django.shortcuts import render
from tasks import test_task
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import Group
from models import CustomUser
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer

@xframe_options_exempt
def home(request):

    return render(request, 'home.html', {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer