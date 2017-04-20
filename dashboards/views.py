from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from validators import DashboardValidator, WidgetValidator
from factories import DashboardFactory, DashboardWidgetFactory

from dashboards.models import Dashboard, DashboardWidget
from dashboards.exceptions import InvalidDashboardParametersException, InvalidWidgetParametersException


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
            dashboard = Dashboard.objects(uuid=request.query_params["uuid"]).first()
            return render_to_response('dashboards/dashboard.html',
                                      {'content_title': dashboard.name, 'dashboards': dashboard,
                                       'widget_types': DashboardWidget.TYPES.keys()},
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

    @staticmethod
    @api_view(['PUT'])
    def put(request):
        try:
            DashboardValidator.validate_params_for_update(request.query_params)
            dashboard = Dashboard.objects(uuid=request.query_params['uuid']).first()
            dashboard.update_with(request.query_params).save()
            return JsonResponse({'message': "Dashboard successfully updated"}, status=200)
        except InvalidDashboardParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)


class Widgets(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            if 'widget-uuid' in request.query_params.keys():
                widget = \
                    Dashboard.objects(widgets__match={'uuid': request.query_params['widget-uuid']}).first().widgets[0]

                return HttpResponse(widget.to_json())
            else:
                return JsonResponse({'message': "The query should contains the following parameters: "
                                                "<widget-uuid>"}, status=400)
        except Exception as e:
            return JsonResponse({'message': e.message}, status=500)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            widget = DashboardWidgetFactory.create_widget_from_query_params(
                    WidgetValidator.validate_params_for_creation(request.query_params))
            dashboard = Dashboard.objects(uuid=request.query_params['dashboard-uuid']).first()
            dashboard.widgets.append(widget)
            dashboard.save()
            return Response(status=status.HTTP_201_CREATED)
        except InvalidDashboardParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        try:
            if 'dashboard-uuid' in request.query_params.keys() and 'widget-uuid' in request.query_params.keys():
                dashboard = Dashboard.objects(uuid=request.query_params['dashboard-uuid'])
                dashboard.update_one(pull__widgets__uuid=DashboardWidget(uuid=request.query_params['widget-uuid']).uuid)
                return JsonResponse({'message': "Widget successfully deleted"}, status=200)
            else:
                return JsonResponse({'message': "The query should contains the following parameters: "
                                                "<dashboard-uuid>, <widget-uuid>"}, status=400)
        except Exception as e:
            return JsonResponse({'message': e.message}, status=500)

    @staticmethod
    @api_view(['PUT'])
    def put(request):
        try:
            Dashboard.objects(uuid=request.query_params['dashboard-uuid'],
                              widgets__uuid=request.query_params['widget-uuid']).update(
                    set__widgets__S__name=request.query_params['name'])
            return JsonResponse({'message': "Widget successfully updated"}, status=200)
        except InvalidWidgetParametersException as e:
            return JsonResponse({'message': "The query should contains the following parameters: "
                                            "<dashboard-uuid>, <widget-uuid>"}, status=400)
        except Exception as e:
            return JsonResponse({'message': e.message}, status=500)
