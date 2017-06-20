from telemetry.exceptions import InvalidSensorParametersException, InvalidMonitoredObjectParametersException, \
    InvalidTransmitterParametersException, InvalidTransmitterInterfaceParametersException, \
    InvalidTransmitterActionParametersException
from telemetry.models import Sensor, MonitoredObject, DeviceInterface


class SensorValidator(object):
    @staticmethod
    def validate_post_parameters_from(query_params):
        SensorValidator.__validate_name_from(query_params)
        SensorValidator.__validate_description_from(query_params)
        SensorValidator.__validate_location_from(query_params)
        SensorValidator.__validate_measure_from(query_params)
        SensorValidator.__validate_type_from(query_params)
        if query_params['location'] == Sensor.LOCATIONS['remote']:
            SensorValidator.__validate_node_from(query_params)
        return query_params

    @staticmethod
    def validate_delete_parameters_from(query_params):
        pass

    @staticmethod
    def __validate_name_from(query_params):
        if 'name' not in query_params.keys() or not query_params['name']:
            raise InvalidSensorParametersException("Parameter <name> should not be null or empty")

    @staticmethod
    def __validate_description_from(query_params):
        # There is no need to validate the description for now
        pass

    @staticmethod
    def __validate_type_from(query_params):
        if 'type' not in query_params.keys() or not query_params['type']:
            raise InvalidSensorParametersException("Parameter <type> should not be null or empty")
        elif query_params['type'] not in Sensor.TYPES.keys():
            raise InvalidSensorParametersException(
                    "Parameter <type> should be one of those:" + str(Sensor.TYPES.keys()))

    @staticmethod
    def __validate_location_from(query_params):
        if 'location' not in query_params.keys() or not query_params['location']:
            raise InvalidSensorParametersException("Parameter <location> should not be null or empty")
        elif query_params['location'] not in Sensor.LOCATIONS.keys():
            raise InvalidSensorParametersException(
                    "Parameter <location> should be one of those:" + str(Sensor.LOCATIONS.keys()))

    @staticmethod
    def __validate_node_from(query_params):
        if 'node' not in query_params.keys() or not query_params['node']:
            raise InvalidSensorParametersException("Parameter <node> should not be null or empty")

    @staticmethod
    def __validate_measure_from(query_params):
        if 'measures' not in query_params.keys() or not query_params['measures']:
            raise InvalidSensorParametersException("Parameter <measures> should not be null or empty")

    @staticmethod
    def __validate_monitored_uuid_from(query_params):
        if 'monitored_object-uuid' not in query_params.keys() or not query_params['monitored_object-uuid']:
            raise InvalidSensorParametersException("Parameter <monitored-object-uuid> should not be null or empty")

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidSensorParametersException("Parameter <uuid> should not be null or empty")


class MonitoredObjectValidator(object):
    @staticmethod
    def validate_get_parameters_from(query_params):
        MonitoredObjectValidator.__validate_uuid_from(query_params)
        return query_params

    @staticmethod
    def validate_post_parameters_from(query_params):
        MonitoredObjectValidator.__validate_name_from(query_params)
        MonitoredObjectValidator.__validate_description_from(query_params)
        MonitoredObjectValidator.__validate_type_from(query_params)
        MonitoredObjectValidator.__validate_id_from(query_params)
        return query_params

    @staticmethod
    def validate_delete_parameters_from(query_params):
        MonitoredObjectValidator.__validate_uuid_from(query_params)
        return query_params

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidMonitoredObjectParametersException("Parameter <uuid> should not be null or empty")

    @staticmethod
    def __validate_name_from(query_params):
        if 'name' not in query_params.keys() or not query_params['name']:
            raise InvalidMonitoredObjectParametersException("Parameter <name> should not be null or empty")

    @staticmethod
    def __validate_description_from(query_params):
        pass

    @staticmethod
    def __validate_type_from(query_params):
        if 'type' not in query_params.keys() or not query_params['type']:
            raise InvalidSensorParametersException("Parameter <type> should not be null or empty")
        elif query_params['type'] not in MonitoredObject.TYPES.keys():
            raise InvalidMonitoredObjectParametersException(
                    "Parameter <type> should be one of those:" + str(MonitoredObject.TYPES.keys()))

    @staticmethod
    def __validate_id_from(query_params):
        if 'id' not in query_params.keys() or not query_params['id']:
            raise InvalidMonitoredObjectParametersException("Parameter <id> should not be null or empty")


class TransmitterValidator(object):
    @staticmethod
    def validate_post_parameters_from(query_params):
        TransmitterValidator.__validate_name_from(query_params)
        TransmitterValidator.__validate_description_from(query_params)
        TransmitterInterfaceValidator.validate_transmitter_interface_parameters_from(query_params)
        return query_params

    @staticmethod
    def validate_delete_parameters_from(query_params):
        TransmitterValidator.__validate_uuid_from(query_params)
        return query_params

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidTransmitterParametersException("Parameter <uuid> should not be null or empty")

    @staticmethod
    def __validate_name_from(query_params):
        if 'name' not in query_params.keys() or not query_params['name']:
            raise InvalidTransmitterParametersException("Parameter <name> should not be null or empty")

    @staticmethod
    def __validate_description_from(query_params):
        pass

    @staticmethod
    def __validate_interface_type_from(query_params):
        if 'interface-type' not in query_params.keys() or not query_params['interface-type']:
            raise InvalidTransmitterParametersException("Parameter <interface-type> should not be null or empty")
        elif query_params['interface-type'] not in DeviceInterface.TYPES.keys():
            raise InvalidMonitoredObjectParametersException(
                    "Parameter <interface-type> should be one of those:" + str(DeviceInterface.TYPES.keys()))


class TransmitterInterfaceValidator(object):
    @staticmethod
    def validate_transmitter_interface_parameters_from(query_params):
        if query_params['interface-type'] == DeviceInterface.TYPES['serial']:
            TransmitterInterfaceValidator.__validate_serial_interface_parameters_from(query_params)

    @staticmethod
    def __validate_serial_interface_parameters_from(query_params):
        TransmitterInterfaceValidator.__validate_baud_rate_from(query_params)
        TransmitterInterfaceValidator.__validate_port_from(query_params)

    @staticmethod
    def __validate_baud_rate_from(query_params):
        if 'baud-rate' not in query_params.keys() or not query_params['baud-rate']:
            raise InvalidTransmitterInterfaceParametersException("Parameter <baud-rate> should not be null or empty")

    @staticmethod
    def __validate_port_from(query_params):
        if 'port' not in query_params.keys() or not query_params['port']:
            raise InvalidTransmitterInterfaceParametersException("Parameter <port> should not be null or empty")


class TransmitterStartValidator(object):
    @staticmethod
    def validate_get_parameters_from(query_params):
        TransmitterStartValidator.__validate_uuid_from(query_params)

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidTransmitterActionParametersException("Parameter <uuid> should not be null or empty")


class TransmitterStopValidator(object):
    @staticmethod
    def validate_get_parameters_from(query_params):
        TransmitterStopValidator.__validate_uuid_from(query_params)

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidTransmitterActionParametersException("Parameter <uuid> should not be null or empty")
