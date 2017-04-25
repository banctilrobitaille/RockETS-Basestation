from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class Telemetry(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        return render_to_response('telemetry/telemetry-index.html', {'content_title': "Telemetry"},
                                  RequestContext(request))
