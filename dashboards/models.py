from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class DashboardType(object):
    AIRCRAFT_DASHBOARD = "aircraft"


class DashboardWidget(EmbeddedDocument):
    uuid = UUIDField(required=True)
    name = StringField(required=True)
    description = StringField()


class Dashboard(Document):
    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    type = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))
