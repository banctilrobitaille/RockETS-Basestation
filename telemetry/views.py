from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from telemetry.exceptions import InvalidSensorParametersException
from telemetry.factories import SensorFactory
from telemetry.models import Sensor, MonitoredObject, RemoteSensor
from telemetry.validators import SensorValidator


class Telemetry(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        return render_to_response('telemetry/telemetry-index.html',
                                  {'content_title': "Telemetry",
                                   'remote_sensors': Sensor.objects.all(),
                                   'sensor_types': Sensor.TYPES.keys(),
                                   'monitored_object_types': MonitoredObject.TYPES.keys()},
                                  RequestContext(request))


class TelemetryMonitoredObjects(APIView):
    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['UPDATE'])
    def update(request):
        try:
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        try:
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)


class TelemetrySensors(APIView):
    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            SensorFactory.create_sensor_from_query_params(
                    SensorValidator.validate(request.query_params)).save()
            return Response(status=status.HTTP_201_CREATED)
        except InvalidSensorParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['UPDATE'])
    def update(request):
        try:
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        try:
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)
