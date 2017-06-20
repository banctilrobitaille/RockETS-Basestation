from telemetry.factories import TransmitterWorkerFactory, DeviceWorkerFactory
from telemetry.models import DeviceInterface


class CommunicationService(object):
    __instance = None

    def __init__(self):
        self.__active_workers = {}

    def start_reception_from(self, device):
        if device.uuid not in self.__active_workers.keys():
            transmitter_worker = TransmitterWorkerFactory.create_transmitter_worker_with(
                    DeviceInterface.objects(uuid=device.interface_id).first())
            transmitter_worker.start()
            self.__active_workers[device.uuid] = transmitter_worker

    def stop_reception_from(self, transmitter):
        if transmitter.uuid in self.__active_workers.keys():
            self.__active_workers[transmitter.uuid].stop()
            del self.__active_workers[transmitter.uuid]

    @staticmethod
    def get_instance():
        if CommunicationService.__instance is None:
            CommunicationService.__instance = CommunicationService()
        return CommunicationService.__instance
