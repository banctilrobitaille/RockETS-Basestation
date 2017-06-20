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
from telemetry.models import Sensor, MonitoredObject, Transmitter, DeviceInterface, LocalSensor
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
                                   'transmitter_interface_types': DeviceInterface.TYPES.keys(),
                                   'sensor_types': Sensor.TYPES.keys(),
                                   'local_sensors': LocalSensor.objects.all()},
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
            MonitoredObjectValidator.validate_delete_parameters_from(request.query_params)
            monitored_object = MonitoredObject.objects(uuid=request.query_params['uuid']).first()

            for sensor_id in monitored_object.sensor_ids:
                try:
                    Sensor.objects(uuid=sensor_id).delete()
                except Exception as e:
                    print("Unable to delete sensor with ID: " + sensor_id)
            monitored_object.delete()
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

            if request.query_params['location'] == Sensor.LOCATIONS['remote']:
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
            SensorValidator.validate_delete_parameters_from(request.query_params)
            if 'monitored-object-uuid' in request.query_params.keys():
                MonitoredObject.objects(uuid=request.query_params['monitored-object-uuid']).update(
                        pull__sensor_ids=request.query_params['uuid'])
            Sensor.objects(uuid=request.query_params['uuid']).delete()
            return Response(status=status.HTTP_200_OK)
        except InvalidSensorParametersException as e:
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

    @staticmethod
    @api_view(['DELETE'])
    def delete(request):
        try:
            TransmitterValidator.validate_delete_parameters_from(request.query_params)
            transmitter = Transmitter.objects(uuid=request.query_params['uuid']).first()
            transmitter_interface = DeviceInterface.objects(uuid=transmitter.interface_id).first()
            transmitter_interface.delete()
            transmitter.delete()
            return Response(status=status.HTTP_200_OK)
        except InvalidSensorParametersException as e:
            return JsonResponse({'error_message': e.message}, status=400)


class TelemetryTransmitterStart(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            TransmitterStartValidator.validate_get_parameters_from(request.query_params)
            CommunicationService.get_instance().start_reception_from(
                    device=Transmitter.objects(uuid=request.query_params['uuid']).first())
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=500)


class TelemetryTransmitterStop(APIView):
    @staticmethod
    @api_view(['GET'])
    def get(request):
        try:
            TransmitterStopValidator.validate_get_parameters_from(request.query_params)
            CommunicationService.get_instance().stop_reception_from(
                    transmitter=Transmitter.objects(uuid=request.query_params['uuid']).first())
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=500)


class TelemetryLocalSensorsStart(APIView):
    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            for local_sensor in LocalSensor.objects.all():
                CommunicationService.get_instance().start_reception_from(local_sensor)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=500)


class TelemetryLocalSensorsStop(APIView):
    @staticmethod
    @api_view(['POST'])
    def post(request):
        try:
            for local_sensor in LocalSensor.objects.all():
                CommunicationService.get_instance().stop_reception_from(local_sensor)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error_message': e.message}, status=500)
