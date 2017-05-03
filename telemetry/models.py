from __future__ import unicode_literals

from mongoengine import *


class Flight(EmbeddedDocument):
    flight_number = IntField()
    start_time = DateTimeField()
    end_time = DateTimeField()
    in_flight_start_time = DateTimeField()
    launch_location = PointField()
    landing_location = PointField()


class MonitoredObject(Document):
    meta = {
        'abstract': True,
    }
    TYPES = {
        'rocket': "Rocket",
        'rocket engine': "Rocket engine"
    }
    uuid = UUIDField(required=True)
    name = StringField(required=True)
    description = StringField()
    identifier = StringField()


class Aircraft(MonitoredObject):
    meta = {
        'abstract': True,
    }
    flights = ListField(EmbeddedDocumentField(Flight))


class Rocket(Aircraft):
    target_altitude = FloatField()


class RocketEngine(MonitoredObject):
    pass


class CommunicationProtocol(Document):
    TYPES = {
        'rockets_custom': "Rockets Custom",
    }


class SensorMeasurement(EmbeddedDocument):
    name = StringField(required=True)


class Sensor(Document):
    meta = {
        'abstract': True,
    }
    TYPES = {
        'barometer': "Barometer",
        'thermometer': "Thermometer",
    }
    LOCATIONS = {
        'remote': "remote",
    }
    name = StringField(required=True)
    uuid = UUIDField(required=True)
    type = StringField(required=True)
    description = StringField()


class RemoteSensor(Sensor):
    measurements = ListField(EmbeddedDocumentField(SensorMeasurement))
    node = StringField(required=True)


class Transmitter(Document):
    name = StringField(required=True)
    uuid = UUIDField(required=True)
    description = StringField()


class DeviceInterface(Document):
    meta = {
        'abstract': True,
    }
    TYPES = {
        'serial': "serial"
    }


class SerialInterface(DeviceInterface):
    BAUD_RATES = {
        '4800': "4800",
        '9600': "9600",
        '57600': "57600",
    }
    baud_rate = StringField(required=True)
    port = StringField(required=True)
