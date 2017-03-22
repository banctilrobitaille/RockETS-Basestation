from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from sensors.models import Sensor


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        context = {
            'content_title': "Sensors",
            'sensors': Sensor.objects.all(),
        }
        return render_to_response('sensors/sensors-index.html', context, RequestContext(request))
