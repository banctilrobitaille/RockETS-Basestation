import serial
from threading import Thread
from channels import Group
import json


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
        """self.__serial_connection = serial.Serial(port='COM5',
                                                 baudrate=57600,
                                                 parity=serial.PARITY_NONE,
                                                 stopbits=serial.STOPBITS_ONE,
                                                 bytesize=serial.EIGHTBITS)"""

    def run(self):
        self.__is_running = True
        while self.__is_running:
            out = ''
            """self.__serial_connection.flush()
            received_string = self.__serial_connection.readline()
            print(received_string)

            try:
                data = json.loads(received_string)
                Group(self.__channel_group).send({'text': str(data['Measures']['Altitude']['Altitude_AGL'])})
            except Exception as e:
                print(e.message)"""


def stop(self):
    self.__is_running = False
