class InvalidSensorParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidMonitoredObjectParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidTransmitterParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidTransmitterInterfaceParametersException(ValueError):
    def __init__(self, message):
        self.message = message


class InvalidTransmitterActionParametersException(ValueError):
    def __init__(self, message):
        self.message = message
