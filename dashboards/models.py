from __future__ import unicode_literals

from mongoengine import *


class DashboardWidget(EmbeddedDocument):
    MINIMUM_WIDTH = 2
    MAXIMUM_WIDTH = 10
    meta = {
        'abstract': True,
    }
    TYPES = {
        'line-chart': "line-chart",
        'altimeter': "altimeter",
        'variometer': "variometer",
        'heading': "heading",
        'airspeed': "airspeed",
        'gauge': "gauge",
        'gps-map': "GPS map",
        'guided-chute-planner': "Guided chute planner",
        'single-value': "Single value",
        'state-machine': "State machine",
        'boolean-state': "Boolean state",
    }
    MEASURE_UNITS = {
        'kn': "kn",
        'm': "m",
        'ft': "ft",
        'm/min': "m/min",
        'm/sec': "m/sec",
        'ft/min': "ft/min",
        'ft/sec': "ft/sec",
        'ft/sec2': "ft/sec2",
        'm/sec2': "m/sec2",
        'none': "none"
    }
    CATEGORIES = {
        'gauge': "gauge",
        'chart': "chart",
        'map': "map"
    }
    TYPES_TO_CATEGORY = {
        'line-chart': "chart",
        'altimeter': "gauge",
        'variometer': "gauge",
        'heading': "gauge",
        'airspeed': "gauge",
        'gauge': "gauge",
        'gps-map': "map",
        'guided-chute-planner': "map",
        'single-value': "single value",
        'state-machine': "State machine",
        'boolean-state': "Boolean state",
    }

    uuid = UUIDField(required=True)
    sensor_id = UUIDField()
    sensor_measure = StringField()
    name = StringField(required=True)
    description = StringField()
    type = StringField()
    category = StringField()
    measure_units = StringField()
    grid_position = IntField(min_value=0)
    width = IntField(min_value=1, max_value=11)
    minValue = FloatField()
    maxValue = FloatField()


class GpsMap(DashboardWidget):
    pass


class Dashboard(Document):
    TEMPLATES = {'none': "none", 'aircraft': "aircraft"}

    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    template = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))
    monitored_object_id = UUIDField(required=True)
    transmitter_id = UUIDField(required=True)

    def update_with(self, params):
        if 'name' in params.keys():
            self.name = params['name']
        if 'description' in params.keys():
            self.description = params['description']

        return self


class DashboardRow(object):
    MAXIMUM_WIDTH = 9

    __number_of_widgets = None
    __used_width = None
    __widgets = None

    def __init__(self):
        self.__number_of_widgets = 0
        self.__used_width = 0
        self.__widgets = []

    @property
    def is_full(self):
        return self.__used_width < DashboardRow.MAXIMUM_WIDTH - DashboardWidget.MINIMUM_WIDTH

    @property
    def widgets(self):
        return self.__widgets

    @property
    def used_width(self):
        return self.__used_width

    def has_room_for(self, widget):
        return self.__used_width + widget.width <= DashboardRow.MAXIMUM_WIDTH

    def add_widget(self, widget):
        if self.has_room_for(widget):
            self.__widgets.append(widget)
            self.__used_width = self.__used_width + widget.width
