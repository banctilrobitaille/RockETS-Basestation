from telemetry.factories import DeviceWorkerFactory


class CommunicationService(object):
    __instance = None

    def __init__(self):
        self.__active_workers = {}

    def start_reception_with(self, device, data_processor):
        if device.uuid not in self.__active_workers.keys():
            device_worker = DeviceWorkerFactory.create_device_worker_with(device, data_processor)
            device_worker.start()
            self.__active_workers[device.uuid] = device_worker

    def stop_reception_from(self, device):
        if device.uuid in self.__active_workers.keys():
            self.__active_workers[device.uuid].stop()
            del self.__active_workers[device.uuid]

    @staticmethod
    def get_instance():
        if CommunicationService.__instance is None:
            CommunicationService.__instance = CommunicationService()
        return CommunicationService.__instance
