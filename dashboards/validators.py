from dashboards.models import Dashboard
from exceptions import InvalidDashboardParametersException


class DashboardValidator(object):
    @staticmethod
    def validate(query_params, for_update=False):
        DashboardValidator.__validate_uuid_from(query_params)
        if not for_update:
            DashboardValidator.__validate_name_from(query_params)
            DashboardValidator.__validate_description_from(query_params)
            DashboardValidator.__validate_template_from(query_params)
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
