from telemetry.exceptions import InvalidSensorParametersException
from telemetry.models import Sensor


class SensorValidator(object):
    @staticmethod
    def validate(query_params):
        SensorValidator.__validate_name_from(query_params)
        SensorValidator.__validate_description_from(query_params)
        SensorValidator.__validate_location_from(query_params)
        SensorValidator.__validate_measure_from(query_params)
        SensorValidator.__validate_node_from(query_params)
        SensorValidator.__validate_type_from(query_params)
        return query_params

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
