class InvalidDashboardParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidWidgetParametersException(ValueError):
    def __init__(self, message):
        self.message = message
