from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class DashboardWidget(EmbeddedDocument):
    TYPES = {'line-chart': "line-chart",
             'altitude-gauge': "altitude-gauge",
             'vertical-speed-gauge': "vertical-speed-gauge",
             'heading-gauge': "heading-gauge",
             'air-speed-gauge': "air-speed-gauge"}
    MEASURE_UNITS = {'knots': "kn",
                     'meters': "m",
                     'feet': "ft",
                     'meters_per_minute': "m/min",
                     'meters_per_second': "m/sec",
                     'feet_per_minute': "ft/min",
                     'feet_per_second': "ft/sec",
                     }

    uuid = UUIDField(required=True)
    sensor_id = UUIDField()
    name = StringField(required=True)
    description = StringField()
    type = StringField()
    measure_units = StringField()
    grid_position = IntField(min_value=0)
    size = IntField(min_value=1, max_value=5)


class Dashboard(Document):
    TEMPLATES = {'none': "none", 'aircraft': "aircraft"}

    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    template = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))
