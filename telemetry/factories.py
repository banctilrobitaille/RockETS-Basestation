import uuid

from telemetry.models import Sensor, RemoteSensor, SensorMeasurement


class SensorFactory(object):
    MEASURES_SEPARATOR = ","

    @staticmethod
    def create_sensor_from_query_params(query_params):
        if query_params['location'] == Sensor.LOCATIONS['remote']:
            sensor = SensorFactory.create_remote_sensor_from(query_params)
        else:
            raise NotImplementedError
        return sensor

    @staticmethod
    def create_remote_sensor_from(query_params):
        remote_sensor = RemoteSensor()
        remote_sensor.name = query_params['name']
        remote_sensor.description = query_params['description']
        remote_sensor.type = query_params['type']
        remote_sensor.node = query_params['node']
        remote_sensor.uuid = uuid.uuid4()

        for measure in query_params['measures'].split(SensorFactory.MEASURES_SEPARATOR):
            remote_sensor_measure = SensorMeasurement()
            remote_sensor_measure.name = measure
            remote_sensor.measurements.append(remote_sensor_measure)

        return remote_sensor

    @staticmethod
    def create_local_sensor_from(query_params):
        return None
