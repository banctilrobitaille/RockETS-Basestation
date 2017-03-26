from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from validators import DashboardValidator
from factories import DashboardFactory

from dashboards.models import Dashboard
from dashboards.exceptions import InvalidDashboardParametersException


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
        try:
            DashboardFactory.create_dashboard_from_query_params(DashboardValidator.validate(request.query_params))
            return Response(status=status.HTTP_201_CREATED)
        except InvalidDashboardParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)
