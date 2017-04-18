from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class DashboardWidget(EmbeddedDocument):
    meta = {
        'abstract': True,
    }

    TYPES = {'line-chart': "line-chart",
             'altimeter': "altimeter",
             'variometer': "variometer",
             'heading': "heading",
             'airspeed': "airspeed",
             'gps-map': "GPS map",
             'guided-chute-planner': "Guided chute planner"}
    MEASURE_UNITS = {'knots': "kn",
                     'meters': "m",
                     'feet': "ft",
                     'meters_per_minute': "m/min",
                     'meters_per_second': "m/sec",
                     'feet_per_minute': "ft/min",
                     'feet_per_second': "ft/sec",
                     }
    CATEGORIES = {'gauge': "gauge",
                  'chart': "chart",
                  'map': "map"}

    TYPES_TO_CATEGORY = {
        'line-chart': "chart",
        'altimeter': "gauge",
        'variometer': "gauge",
        'heading': "gauge",
        'airspeed': "gauge",
        'gps-map': "map",
        'guided-chute-planner': "map"
    }

    uuid = UUIDField(required=True)
    sensor_id = UUIDField()
    name = StringField(required=True)
    description = StringField()
    type = StringField()
    category = StringField()
    measure_units = StringField()
    grid_position = IntField(min_value=0)
    size = IntField(min_value=1, max_value=5)


class GpsMap(DashboardWidget):
    pass


class Dashboard(Document):
    TEMPLATES = {'none': "none", 'aircraft': "aircraft"}

    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    template = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))

    def update_with(self, params):
        if 'name' in params.keys():
            self.name = params['name']
        if 'description' in params.keys():
            self.description = params['description']

        return self
