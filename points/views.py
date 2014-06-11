import urllib
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django_facebook.api import require_persistent_graph
from django.http import HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import Group
from models import CustomUser, Transaction
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer
from django.forms import ModelForm
from django.core.urlresolvers import reverse
import json
from serializers import FacebookUserSerializer
import requests
from django_facebook.decorators import facebook_required
from django import forms
import re

class TransactionForm(forms.Form):
    points = forms.IntegerField(min_value=0,max_value=100)
    message = forms.CharField()
    image = forms.ImageField()


class ReadOnlyFieldsMixin(object):
    readonly_fields = ()

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldsMixin, self).__init__(*args, **kwargs)
        for field in (field for name, field in self.fields.iteritems() if name in self.Meta.readonly_fields):
            field.widget.attrs['disabled'] = 'true'
            field.required = False

    def clean(self):
        cleaned_data = super(ReadOnlyFieldsMixin, self).clean()
        for field in self.Meta.readonly_fields:
            cleaned_data[field] = getattr(self.instance, field)

        return cleaned_data

@xframe_options_exempt
@facebook_required()
def home(request):
    return render(request, 'home.html')


@facebook_required()
def search_results(request):
    facebook = require_persistent_graph(request)
    search_term = request.POST.get("search_term")

    search_term = search_term.strip()
    terms = re.sub("\s+"," ",search_term).split(" ")

    friend_set = request.user.friends()
    for term in terms:
        friend_set = friend_set.filter(name__icontains=term)

    friends = friend_set.all()

    url = "https://graph.facebook.com/search?q={}&type=user&access_token={}".format(
        urllib.quote_plus(search_term),
        facebook.access_token)

    result = requests.get(url)
    users = json.loads(result.content)['data']
    return render(request, 'search_results.html', {'users': users})

@facebook_required()
def transaction(request):
    if request.method == 'POST': # If the form has been submitted...
         # ContactForm was defined in the the previous section
        form = TransactionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = TransactionForm() # An unbound form

    return render(request, 'transaction.html', {'form': form})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer