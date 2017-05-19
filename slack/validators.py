from slack.exceptions import InvalidSlackOAuthParametersException


class SlackOAuthValidator(object):
    @staticmethod
    def validate_get_parameters_from(query_params):
        SlackOAuthValidator.__validate_code_from(query_params)
        return query_params

    @staticmethod
    def __validate_code_from(query_params):
        if 'code' not in query_params.keys() or not query_params['code']:
            raise InvalidSlackOAuthParametersException("Parameter <code> should not be null or empty")
