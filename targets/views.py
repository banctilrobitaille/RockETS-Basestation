from django.shortcuts import render_to_response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.template import RequestContext


class Targets(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        return render_to_response('targets/targets-index.html', {'content_title': "Monitored Objects"}, RequestContext(request))
