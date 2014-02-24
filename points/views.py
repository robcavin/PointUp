from django.shortcuts import render_to_response
from tasks import test_task
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def home(request):
    test_task.delay()
    return render_to_response('base.html', {})