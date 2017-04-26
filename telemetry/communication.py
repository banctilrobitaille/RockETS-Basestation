import random
from threading import Thread

import time
from channels import Group


class CommunicationService(object):
    __instance = None

    def __init__(self):
        self.__active_communication_devices = {}

    def open_communication_channel_for(self, device):
        device_worker = CommunicationDeviceWorker(device)
        device_worker.start()
        self.__active_communication_devices[str(device)] = device_worker

    def close_communication_channel_of(self, device):
        self.__active_communication_devices[device].stop()

    @staticmethod
    def get_instance():
        if CommunicationService.__instance is None:
            CommunicationService.__instance = CommunicationService()
        return CommunicationService.__instance


class CommunicationDevice(object):
    def __init__(self):
        pass


class SerialCommunicationDevice(object):
    def __init__(self):
        pass


class CommunicationDeviceWorker(Thread):
    def __init__(self, channel_group):
        super(CommunicationDeviceWorker, self).__init__()
        self.__is_running = False
        self.__channel_group = channel_group

    def run(self):
        self.__is_running = True
        while self.__is_running:
            Group(self.__channel_group).send({'text': str(random.uniform(0.0, 100.0))})
            time.sleep(2)

    def stop(self):
        self.__is_running = False
