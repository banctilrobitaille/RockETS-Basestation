from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from telemetry.communication import CommunicationService
from telemetry.exceptions import InvalidSensorParametersException, InvalidMonitoredObjectParametersException
from telemetry.factories import SensorFactory, MonitoredObjectFactory, TransmitterFactory
from telemetry.models import Sensor, MonitoredObject, RemoteSensor, Transmitter, TransmitterInterface
from telemetry.validators import SensorValidator, MonitoredObjectValidator, TransmitterValidator, \
    TransmitterStartValidator, TransmitterStopValidator


class Telemetry(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        return render_to_response('telemetry/telemetry-index.html',
                                  {'content_title': "Telemetry",
                                   'monitored_objects': MonitoredObject.objects.all(),
                                   'monitored_object_types': MonitoredObject.TYPES.keys(),
                                   'transmitters': Transmitter.objects.all(),
                                   'transmitter_interface_types': TransmitterInterface.TYPES.keys()},
                                  RequestContext(request))


class TelemetryMonitoredObjects(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            MonitoredObjectValidator.validate_get_parameters_from(request.query_params)
            monitored_object = MonitoredObject.objects(uuid=request.query_params['uuid']).first()
            return render_to_response('telemetry/monitored-object-index.html',
                                      {'content_title': monitored_object.name,
                                       'monitored_object': monitored_object,
                                       'sensors': map(lambda sensor_id: Sensor.objects(uuid=sensor_id).first(),
                                                      monitored_object.sensor_ids),
                                       'sensor_types': Sensor.TYPES.keys()},
                                      RequestContext(request))
        except InvalidMonitoredObjectParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            MonitoredObjectFactory.create_monitored_object_from(
                    MonitoredObjectValidator.validate_post_parameters_from(request.query_params)).save()
            return Response(status=status.HTTP_201_CREATED)
        except InvalidMonitoredObjectParametersException as e:
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
    @api_view(['GET'])
    def get(request):
        try:
            return HttpResponse(Sensor.objects(uuid=request.query_params['uuid']).first().to_json())
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=400)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            sensor = SensorFactory.create_sensor_from_query_params(
                    SensorValidator.validate_post_parameters_from(request.query_params))
            monitored_object = MonitoredObject.objects(uuid=request.query_params['monitored-object-uuid']).first()
            monitored_object.sensor_ids.append(sensor.uuid)
            monitored_object.save()
            sensor.save()
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


class TelemetryTransmitters(APIView):
    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            TransmitterFactory.create_transmitter_from(
                    TransmitterValidator.validate_post_parameters_from(request.query_params)).save()
            return Response(status=status.HTTP_201_CREATED)
        except InvalidSensorParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)


class TelemetryTransmitterStart(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            TransmitterStartValidator.validate_get_parameters_from(request.query_params)
            CommunicationService.get_instance().start_reception_with(
                    Transmitter.objects(uuid=request.query_params['uuid']).first())
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            pass


class TelemetryTransmitterStop(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            TransmitterStopValidator.validate_get_parameters_from(request.query_params)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            pass
