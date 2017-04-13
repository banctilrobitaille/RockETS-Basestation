from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class DashboardTemplates(object):
    NAME = ["aircraft"]


class DashboardWidget(EmbeddedDocument):
    TYPE = ["line-chart", "altitude-gauge", "vertical-speed-gauge", "heading-gauge", "air-speed-gauge"]

    uuid = UUIDField(required=True)
    sensor_id = UUIDField()
    name = StringField(required=True)
    description = StringField()
    type = StringField()
    measure_units = StringField()
    grid_position = IntField(min_value=1)
    size = IntField(min_value=1, max_value=5)


class Dashboard(Document):
    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    template = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))
