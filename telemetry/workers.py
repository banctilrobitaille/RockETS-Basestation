import serial
from threading import Thread
from channels import Group
import json

from logger.models import LogData
from logger.services import LogService


class DeviceWorker(Thread):
    def __init__(self, data_processor):
        super(DeviceWorker, self).__init__()
        self.__data_processor = data_processor
        self.__is_running = False

    @property
    def data_processor(self):
        return self.__data_processor

    @data_processor.setter
    def data_processor(self, data_processor):
        self.data_processor = data_processor

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, value):
        self.__is_running = value

    def stop(self):
        pass


class SerialTransmitterWorker(DeviceWorker):
    def __init__(self, serial_port, baud_rate):
        super(SerialTransmitterWorker, self).__init__(None)
        self.__serial_connection = serial.Serial(port=serial_port,
                                                 baudrate=baud_rate,
                                                 parity=serial.PARITY_NONE,
                                                 stopbits=serial.STOPBITS_ONE,
                                                 bytesize=serial.EIGHTBITS)

    def run(self):
        self.is_running = True
        self.__serial_connection.flush()
        while self.is_running:
            try:
                if self.__serial_connection.inWaiting() > 0:
                    received_string = self.__serial_connection.readline()
                    raw_data = json.loads(received_string)
                    sensors = raw_data['Sensors']
                    for sensor in sensors.keys():
                        for measure in sensors[sensor]:
                            Group("main-state").send({'text': str(raw_data['Rocket_State']).replace("_", " ")})
                            Group(sensor + "-" + measure).send({'text': str(sensors[sensor][measure])})
            except Exception as e:
                print(e.message)

    def stop(self):
        self.is_running = False
        self.__serial_connection.close()


class SerialDeviceWorker(DeviceWorker):
    def __init__(self, device, data_processor, serial_port, baud_rate):
        super(SerialDeviceWorker, self).__init__(data_processor)
        self.__serial_connection = serial.Serial(port=serial_port,
                                                 baudrate=baud_rate,
                                                 parity=serial.PARITY_NONE,
                                                 stopbits=serial.STOPBITS_ONE,
                                                 bytesize=serial.EIGHTBITS)
        self.device = device

    def run(self):
        self.is_running = True
        self.__serial_connection.flush()
        while self.is_running:
            try:
                if self.__serial_connection.inWaiting() > 0:
                    processed_data = self.data_processor.process(self.__serial_connection.readline())
                    if processed_data is not None:
                        for key, value in processed_data.iteritems():
                            Group(str(self.device.uuid) + "-" + key).send({'text': str(value)})
                        LogService.get_instance().log_data_for(device_type=self.device.type, data=processed_data)
            except Exception as e:
                print(e)

    def stop(self):
        self.is_running = False
        self.__serial_connection.close()
