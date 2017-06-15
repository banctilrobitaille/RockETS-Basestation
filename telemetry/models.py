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
        'allow_inheritance': True,
    }
    TYPES = {
        'rocket': "rocket",
    }
    uuid = UUIDField(required=True)
    name = StringField(required=True)
    description = StringField()
    identifier = StringField(required=True, unique=True)
    sensor_ids = ListField(UUIDField())


class Aircraft(MonitoredObject):
    meta = {
        'allow_inheritance': True,
    }
    flights = ListField(EmbeddedDocumentField(Flight))


class Rocket(Aircraft):
    target_altitude = FloatField()


class RocketEngine(MonitoredObject):
    pass


class SensorMeasurement(EmbeddedDocument):
    name = StringField(required=True)


class Sensor(Document):
    meta = {
        'allow_inheritance': True,
    }
    TYPES = {
        'barometer': "Barometer",
        'thermometer': "Thermometer",
        'altimeter': "altimeter",
        'gps': "gps",
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
    interface_id = UUIDField(required=True)
    # dashboard_id = UUIDField(required=True)


class TransmitterInterface(Document):
    meta = {
        'allow_inheritance': True,
    }
    TYPES = {
        'serial': "serial",
    }
    uuid = UUIDField(required=True)


class SerialTransmitterInterface(TransmitterInterface):
    BAUD_RATES = {
        '4800': "4800",
        '9600': "9600",
        '57600': "57600",
    }
    baud_rate = StringField(required=True)
    port = StringField(required=True)
    type = StringField(default="serial")
