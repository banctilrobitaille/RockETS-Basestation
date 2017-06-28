from logger.models import LogData


class LogService(object):
    __INSTANCE = None

    def log_data_for(self, device_type, data):
        LogData(device_type=device_type, measures=data).save()

    @staticmethod
    def get_instance():
        if LogService.__INSTANCE is None:
            return LogService()
        else:
            return LogService.__INSTANCE
