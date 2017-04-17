from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class Sensor(Document):
    uuid = UUIDField(required=True)
    name = StringField(required=True)
    description = StringField(max_length=200)
    type = StringField(required=True)
    location = StringField(required=True)
    model = StringField(required=True)
    interface = StringField(required=True)
    port = StringField(required=True)
    associatedTag = StringField(required=True)
