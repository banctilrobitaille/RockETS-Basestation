from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
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
        if "uuid" not in request.query_params.keys():
            dashboards = Dashboard.objects.all()
            return render_to_response('dashboards/dashboards-index.html',
                                      {'content_title': "Dashboards", 'dashboards': dashboards},
                                      RequestContext(request))
        else:
            dashboard = Dashboard.objects(uuid=request.query_params["uuid"])
            return render_to_response('dashboards/dashboard.html',
                                      {'content_title': dashboard.name, 'dashboards': dashboard},
                                      RequestContext(request))

    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            DashboardFactory.create_dashboard_from_query_params(
                    DashboardValidator.validate(request.query_params)).save()
            return Response(status=status.HTTP_201_CREATED)
        except InvalidDashboardParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        try:
            if 'uuid' in request.query_params.keys():
                dashboard = Dashboard.objects(uuid=request.query_params['uuid'])
                dashboard.delete()
                return JsonResponse({'message': "Dashboard successfully deleted"}, status=200)
            else:
                return JsonResponse({}, status=400)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=500)
