from telemetry.factories import TransmitterWorkerFactory
from telemetry.models import TransmitterInterface


class CommunicationService(object):
    __instance = None

    def __init__(self):
        self.__active_transmitter_workers = {}

    def start_reception_with(self, transmitter):
        if transmitter.uuid not in self.__active_transmitter_workers.keys():
            transmitter_worker = TransmitterWorkerFactory.create_transmitter_worker_with(
                    TransmitterInterface.objects(uuid=transmitter.interface_id).first())
            transmitter_worker.start()
            self.__active_transmitter_workers[transmitter.uuid] = transmitter_worker

    def stop_reception_from(self, transmitter):
        if transmitter.uuid in self.__active_transmitter_workers.keys():
            self.__active_transmitter_workers[transmitter.uuid].stop()
            del self.__active_transmitter_workers[transmitter.uuid]

    @staticmethod
    def get_instance():
        if CommunicationService.__instance is None:
            CommunicationService.__instance = CommunicationService()
        return CommunicationService.__instance
