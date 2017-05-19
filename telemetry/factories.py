import uuid

from telemetry.models import Sensor, RemoteSensor, SensorMeasurement, MonitoredObject, Rocket, TransmitterInterface, \
    SerialTransmitterInterface, Transmitter
from telemetry.workers import SerialTransmitterWorker


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


class MonitoredObjectFactory(object):
    @staticmethod
    def create_monitored_object_from(query_params):
        monitored_object = None

        if query_params['type'] == MonitoredObject.TYPES['rocket']:
            monitored_object = Rocket()
            monitored_object.name = query_params['name']
            monitored_object.description = query_params['description']
            monitored_object.identifier = query_params['id']
            monitored_object.uuid = uuid.uuid4()
            monitored_object.target_altitude = 0

        return monitored_object


class TransmitterFactory(object):
    @staticmethod
    def create_transmitter_from(query_params):
        transmitter = Transmitter()
        transmitter.name = query_params['name']
        transmitter.description = query_params['description']
        transmitter.uuid = uuid.uuid4()

        transmitter_interface = TransmitterInterfaceFactory.create_transmitter_interface_from(query_params)
        transmitter.interface_id = transmitter_interface.uuid
        transmitter_interface.save()

        return transmitter


class TransmitterInterfaceFactory(object):
    @staticmethod
    def create_transmitter_interface_from(query_params):
        transmitter_interface = None

        if query_params['interface-type'] == TransmitterInterface.TYPES['serial']:
            transmitter_interface = SerialTransmitterInterface()
            transmitter_interface.baud_rate = query_params['baud-rate']
            transmitter_interface.port = query_params['port']
            transmitter_interface.uuid = uuid.uuid4()

        return transmitter_interface


class TransmitterWorkerFactory(object):
    @staticmethod
    def create_transmitter_worker_with(transmitter_interface):
        if transmitter_interface.type == TransmitterInterface.TYPES['serial']:
            return SerialTransmitterWorker(serial_port=transmitter_interface.port,
                                           baud_rate=transmitter_interface.baud_rate)
