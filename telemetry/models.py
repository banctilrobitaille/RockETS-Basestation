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
    TYPES = {'rocket': "Rocket",
             'rocket-engine': "Rocket engine"}
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


class Sensor(Document):
    TYPES = {
        'main_input': "Main input",
        'barometer': "Barometer",
        'thermometer': "Thermometer",
    }
    name = StringField(required=True)
    uuid = UUIDField(required=True)
    measurements = ListField(EmbeddedDocumentField(SensorMeasurement))


class SensorMeasurement(EmbeddedDocument):
    name = StringField()


class SensorInterface(EmbeddedDocument):
    meta = {
        'abstract': True,
    }
    TYPES = {
        'serial': "Serial",
        'network': "Network"
    }
