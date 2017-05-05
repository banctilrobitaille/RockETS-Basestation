class InvalidSensorParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidMonitoredObjectParametersException(ValueError):
    def __init__(self, message):
        self.message = message
