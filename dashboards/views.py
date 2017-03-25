from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from dashboards.models import Dashboard


class Dashboards(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        dashboards = Dashboard.objects.all()
        return render_to_response('dashboards/dashboards-index.html',
                                  {'content_title': "Dashboards", 'dashboards': dashboards}, RequestContext(request))

    @staticmethod
    @api_view(['POST'])
    def post(request):
        return Response(status=status.HTTP_200_OK)
