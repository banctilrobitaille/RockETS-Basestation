import uuid

from telemetry.data_processors import GPSNMEADataProcessor
from telemetry.gps import GPGGASentence
from telemetry.models import RemoteSensor, SensorMeasurement, MonitoredObject, Rocket, DeviceInterface, \
    SerialDeviceInterface, Transmitter, LocalSensor, Sensor
from telemetry.workers import SerialTransmitterWorker, SerialDeviceWorker


class SensorFactory(object):
    MEASURES_SEPARATOR = ","

    @staticmethod
    def create_sensor_from_query_params(query_params):
        if query_params['location'] == Sensor.LOCATIONS['remote']:
            sensor = SensorFactory.create_remote_sensor_from(query_params)
        else:
            sensor = SensorFactory.create_local_sensor_from(query_params)
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
        local_sensor = LocalSensor()
        local_sensor.name = query_params['name']
        local_sensor.description = query_params['description']
        local_sensor.type = query_params['type']
        local_sensor.uuid = uuid.uuid4()

        for measure in query_params['measures'].split(SensorFactory.MEASURES_SEPARATOR):
            local_sensor_measure = SensorMeasurement()
            local_sensor_measure.name = measure
            local_sensor.measurements.append(local_sensor_measure)

        local_sensor_interface = InterfaceFactory.create_interface_from(query_params)
        local_sensor.interface_id = local_sensor_interface.uuid
        local_sensor_interface.save()

        return local_sensor


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

        transmitter_interface = InterfaceFactory.create_interface_from(query_params)
        transmitter.interface_id = transmitter_interface.uuid
        transmitter_interface.save()

        return transmitter


class InterfaceFactory(object):
    @staticmethod
    def create_interface_from(query_params):
        device_interface = None

        if query_params['interface-type'] == DeviceInterface.TYPES['serial']:
            device_interface = SerialDeviceInterface()
            device_interface.baud_rate = query_params['baud-rate']
            device_interface.port = query_params['port']
            device_interface.uuid = uuid.uuid4()

        return device_interface


class TransmitterWorkerFactory(object):
    @staticmethod
    def create_transmitter_worker_with(transmitter_interface):
        if transmitter_interface.type == DeviceInterface.TYPES['serial']:
            return SerialTransmitterWorker(serial_port=transmitter_interface.port,
                                           baud_rate=transmitter_interface.baud_rate)


class DeviceWorkerFactory(object):
    @staticmethod
    def create_device_worker_with(device, data_processor):
        device_interface = DeviceInterface.objects(uuid=device.interface_id).first()
        if device_interface.type == DeviceInterface.TYPES['serial']:
            if data_processor is None:
                return SerialTransmitterWorker(serial_port=device_interface.port,
                                               baud_rate=device_interface.baud_rate)
            else:
                return SerialDeviceWorker(serial_port=device_interface.port,
                                          baud_rate=device_interface.baud_rate,
                                          data_processor=data_processor,
                                          device=device)


class DataProcessorFactory(object):
    @staticmethod
    def create_data_processor_for(device):
        data_processor = None
        if device.type == Sensor.TYPES['gps']:
            data_processor = GPSNMEADataProcessor()

        return data_processor
