from dashboards.models import Dashboard, DashboardWidget
from exceptions import InvalidDashboardParametersException, InvalidWidgetParametersException


class DashboardValidator(object):
    @staticmethod
    def validate(query_params):
        DashboardValidator.__validate_name_from(query_params)
        DashboardValidator.__validate_description_from(query_params)
        DashboardValidator.__validate_template_from(query_params)
        return query_params

    @staticmethod
    def validate_params_for_update(query_params):
        DashboardValidator.__validate_uuid_from(query_params)
        DashboardValidator.__validate_name_from(query_params)
        DashboardValidator.__validate_description_from(query_params)
        return query_params

    @staticmethod
    def __validate_uuid_from(query_params):
        if 'uuid' not in query_params.keys() or not query_params['uuid']:
            raise InvalidDashboardParametersException("Parameter <uuid> should should not be null or empty")

    @staticmethod
    def __validate_name_from(query_params):
        if 'name' not in query_params.keys() or not query_params['name']:
            raise InvalidDashboardParametersException("Parameter <name> should not be null or empty")

    @staticmethod
    def __validate_description_from(query_params):
        pass

    @staticmethod
    def __validate_template_from(query_params):
        if 'template' not in query_params.keys() or not query_params['template']:
            raise InvalidDashboardParametersException("Parameter <template> should not be null or empty")
        elif query_params['template'] not in Dashboard.TEMPLATES.keys():
            raise InvalidDashboardParametersException(
                    "Parameter <template> should be one of those:" + str(Dashboard.TEMPLATES.keys()))


class WidgetValidator(object):
    WIDGET_SIZE_LOWER_BOUND = 2
    WIDGET_SIZE_UPPER_BOUND = 11

    @staticmethod
    def validate_params_for_creation(query_params):
        WidgetValidator.__validate_name_from(query_params)
        WidgetValidator.__validate_description_from(query_params)
        WidgetValidator.__validate_type_from(query_params)
        WidgetValidator.__validate_size_from(query_params)
        WidgetValidator.__validate_dashboard_from(query_params)
        WidgetValidator.__validate_sensor_from(query_params)
        WidgetValidator.__validate_refresh_rate_from(query_params)
        return query_params

    @staticmethod
    def validate_params_for_update(query_params):
        pass

    @staticmethod
    def __validate_name_from(query_params):
        if 'name' not in query_params.keys() or not query_params['name']:
            raise InvalidWidgetParametersException("Parameter <name> should not be null or empty")

    @staticmethod
    def __validate_description_from(query_params):
        pass

    @staticmethod
    def __validate_type_from(query_params):
        if 'type' not in query_params.keys() or not query_params['type']:
            raise InvalidWidgetParametersException("Parameter <type> should not be null or empty")
        elif query_params['type'] not in DashboardWidget.TYPES.keys():
            raise InvalidWidgetParametersException(
                    "Parameter <type> should be one of those:" + str(DashboardWidget.TYPES.keys()))

    @staticmethod
    def __validate_size_from(query_params):
        if 'size' not in query_params.keys() or not query_params['size']:
            raise InvalidWidgetParametersException("Parameter <size> should not be null or empty")
        elif int(query_params['size']) < WidgetValidator.WIDGET_SIZE_LOWER_BOUND or int(
                query_params['size']) > WidgetValidator.WIDGET_SIZE_UPPER_BOUND:
            raise InvalidWidgetParametersException(
                    "Parameter <size> should be in range:" + str(WidgetValidator.WIDGET_SIZE_LOWER_BOUND) + "-" + str(
                            WidgetValidator.WIDGET_SIZE_UPPER_BOUND))

    @staticmethod
    def __validate_dashboard_from(query_params):
        if 'dashboard-uuid' not in query_params.keys() or not query_params['dashboard-uuid']:
            raise InvalidWidgetParametersException("Parameter <dashboard-uuid> should not be null or empty")

    @staticmethod
    def __validate_sensor_from(query_params):
        if 'sensor' not in query_params.keys() or not query_params['sensor']:
            raise InvalidWidgetParametersException("Parameter <sensor> should not be null or empty")

    @staticmethod
    def __validate_refresh_rate_from(query_params):
        if 'refresh-rate' not in query_params.keys() or not query_params['refresh-rate']:
            raise InvalidWidgetParametersException("Parameter <refresh-rate> should not be null or empty")
