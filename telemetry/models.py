from __future__ import unicode_literals

from mongoengine import *


class Flights(EmbeddedDocument):
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


class Aircraft(MonitoredObject):
    meta = {
        'abstract': True,
    }
    flights = ListField(EmbeddedDocumentField(Flights))


class Rocket(Aircraft):
    target_altitude = FloatField()


class RocketEngine(MonitoredObject):
    pass


class CommunicationProtocol(Document):
    pass
