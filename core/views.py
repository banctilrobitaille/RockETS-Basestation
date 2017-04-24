from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class Core(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        return render_to_response('core/home.html', {'content_title': "Home"}, RequestContext(request))
