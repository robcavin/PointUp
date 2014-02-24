from django.shortcuts import render_to_response
from tasks import test_task

def home(request):
    test_task.delay()
    return render_to_response('base.html', {})