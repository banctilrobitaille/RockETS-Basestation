import serial
from threading import Thread
from channels import Group
import json


class TransmitterWorker(Thread):
    def __init__(self):
        super(TransmitterWorker, self).__init__()
        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, value):
        self.__is_running = value

    def stop(self):
        pass


class SerialTransmitterWorker(TransmitterWorker):
    def __init__(self, serial_port, baud_rate):
        super(SerialTransmitterWorker, self).__init__()
        self.__serial_connection = serial.Serial(port=serial_port,
                                                 baudrate=baud_rate,
                                                 parity=serial.PARITY_NONE,
                                                 stopbits=serial.STOPBITS_ONE,
                                                 bytesize=serial.EIGHTBITS)

    def run(self):
        self.is_running = True
        while self.is_running:
            self.__serial_connection.flush()
            received_string = self.__serial_connection.readline()
            try:
                print(received_string)
                raw_data = json.loads(received_string)
                sensors = raw_data['Sensors']
                print(raw_data)
                for sensor in sensors.keys():
                    for measure in sensors[sensor]:
                        Group("main-state").send({'text': str(raw_data['State']).replace("_", " ")})
                        Group(sensor + "-" + measure).send({'text': str(sensors[sensor][measure])})
            except Exception as e:
                print(e.message)

    def stop(self):
        self.is_running = False
        self.__serial_connection.close()
