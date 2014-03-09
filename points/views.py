from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework.renderers import JSONRenderer
from tasks import test_task
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import Group
from models import CustomUser
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer
from django.forms import ModelForm
from django.core.urlresolvers import reverse
import json
from serializers import FacebookUserSerializer

class ReadOnlyFieldsMixin(object):
    readonly_fields =()

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldsMixin, self).__init__(*args, **kwargs)
        for field in (field for name, field in self.fields.iteritems() if name in self.Meta.readonly_fields):
            field.widget.attrs['disabled'] = 'true'
            field.required = False

    def clean(self):
        cleaned_data = super(ReadOnlyFieldsMixin,self).clean()
        for field in self.Meta.readonly_fields:
           cleaned_data[field] = getattr(self.instance, field)

        return cleaned_data

@xframe_options_exempt
@login_required(login_url='facebook/example/')
def home(request):
    class CustomUserForm(ReadOnlyFieldsMixin, ModelForm):
        class Meta:
            model = CustomUser
            fields = ('username','points')
            readonly_fields = ('username','points')

    form = CustomUserForm(instance=request.user)
    friends = JSONRenderer().render(FacebookUserSerializer(request.user.friends(),many=True).data)
    return render(request, 'home.html', {'form':form,'friends':mark_safe(friends)})

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