from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from sensors.models import Sensor


class Sensors(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        context = {
            'content_title': "Sensors",
            'sensors': Sensor.objects.all(),
        }
        return render_to_response('sensors/sensors-index.html', context, RequestContext(request))
