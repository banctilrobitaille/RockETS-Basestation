from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class DashboardTemplates(object):
    NAME = ["aircraft"]


class DashboardWidget(EmbeddedDocument):
    uuid = UUIDField(required=True)
    name = StringField(required=True)
    description = StringField()


class Dashboard(Document):
    uuid = UUIDField(required=True)
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=200)
    template = StringField()
    widgets = ListField(EmbeddedDocumentField(DashboardWidget))
